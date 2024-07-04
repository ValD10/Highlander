import pandas as pd
import requests as rq
import time as tm
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Função de criação da url
def urlcreator(r = " ",n = "SN",b = " ",c = " ",u = " ",cp = " "):
    
    url = f"""https://www.google.com/maps/search/{r.replace(" ","+")}+{n}+{b.replace(" ","+")}+{c.replace(" ","-")}+{u.replace(" ","+")}+{cp}/"""
    return url

#Documento lido
sheet = pd.read_excel("Scrap-BaseMaps.xlsx")
print("Checkpoint Arquivo Lido")    

colunas = ["ENDEREÇO","NÚMERO","BAIRRO","CIDADE","UF","CEP","LATITUDE","LONGITUDE","LINK"]
i = 1

#Loop de criação
for index, row in sheet.iterrows():
    try: 
        # tm.sleep(2)
        #   Colunas Extraídas
        # log = row["LOGRADOURO"]
        end = row["ENDEREÇO"]
        num = row["NÚMERO"]
        bai = row["BAIRRO"]
        cid = row["CIDADE"]
        est = row["UF"]
        cep = row["CEP"]
        lat = row["LATITUDE"]
        lon = row["LONGITUDE"]
        lin = row["LINK"]

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
            laf = str(latfinal.replace(".", ","))
            lof = str(lonfinal.replace(".", ","))
            sheet.at[index, "LATITUDE"] = laf
            sheet.at[index, "LONGITUDE"] = lof
            sheet.at[index, "LINK"] = url
            print(f"Checkpoint Coleta: {laf,lof}")
            i = i+1
    except: 
         i = i+1
         print(f"Falha {i}")
         pass
        
sheet.to_excel("MSD_Base_Geolocalizado.xlsx", index=False)
print(f"Cabei na passagem {i}")
