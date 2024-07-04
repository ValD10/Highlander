import time         as tm
import pyautogui    as pa

pa.hotkey("ctrl","win","left")
chrome = ("win","1")
search = (255,149)
url = (432,60)
excel = ("win","5")
vsc = (1353,179)
pa.hotkey(chrome)

def highlander():
    pa.hotkey(excel)
    tm.sleep(0.5)
    pa.hotkey("ctrl","c")
    pa.hotkey(chrome)
    tm.sleep(0.5)
    pa.moveTo(search)
    pa.click()
    pa.hotkey("ctrl","a")
    pa.hotkey("ctrl","v")
    pa.press("enter")
#    tm.sleep(1.7)
    pa.moveTo(url)
    tm.sleep(3.2)
    pa.click()
    pa.hotkey("ctrl","c")
    pa.hotkey(excel)
    tm.sleep(0.3)
    pa.press("tab")
    pa.press("F2")
    pa.hotkey("ctrl","v")
    pa.press("enter")
    tm.sleep(1.2)
    pa.hotkey(chrome)
    

while 1==1:
    highlander()