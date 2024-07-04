import polars as pl
import requests as rq
import time as tm
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Função de criação da url
def urlcreator(r = " ",n = "SN",b = " ",c = " ",u = " ",cp = " "):
    
    url = f"""https://www.google.com/maps/search/{r.replace(" ","+")}+{n.replace(" ","+")}+{b.replace(" ","+")}+{c.replace(" ","-")}+{u.replace(" ","+")}+{cp}/"""
    return url

#Documento lido
sheet = pl.read_excel("VSC\\Highlander\\Scrap-BaseMaps.xlsx")
print("Checkpoint Arquivo Lido")

colunas = ["ENDEREÇO","NÚMERO","BAIRRO","CIDADE","UF","CEP","LATITUDE","LONGITUDE","LINK"]
i = 1

#Loop de criação
for row in sheet.select(colunas).iter_rows():
    # try: 
        #   Colunas Extraídas
        # log = row["LOGRADOURO"]
        end = row[0]
        num = row[1]
        bai = row[2]
        cid = row[3]
        est = row[4]
        cep = row[5]
        lat = row[6]
        lon = row[7]
        lin = row[8]
        print(f"Checkpoint Passagem {i}")

        #Criando a Url
        url = urlcreator(end,num,cid,est,cep)
        r = rq.get(url)
        print(url)

        #Verificação de Erro
        if r.status_code == 200:
            Chrome_options = Options()
            Chrome_options.headless = True 
            options = wd.ChromeOptions()
            options.add_argument("--headless=new")
            navegador = wd.Chrome(options=options)
            navegador.maximize_window()
            navegador.get(url)
            tm.sleep(0.5)
            valor = navegador.find_element(By.XPATH,"/html/head/meta[5]").get_attribute("content")
            latsplitone = valor.split("https://maps.google.com/maps/api/staticmap?center=")[1]
            lonsplitone = latsplitone.split("%2C")[1]
            latfinal = latsplitone.split("%")[0]
            lonfinal = lonsplitone.split("&")[0]
            # print(url, latfinal,lonfinal)
            laf = latfinal.replace(".", ",")
            lof = lonfinal.replace(".", ",")
            sheet.insert(6,laf)
            sheet.insert_column(7,lof)
            sheet.insert_column(8,url)
            print(f"Checkpoint Coleta: {cep}")
            i = i+1
    # except: 
    #     pass
        

sheet.write_excel("VSC\\Highlander\\Tecban_Fase_III-IV_Geolocalizado.xlsx", index=False)
