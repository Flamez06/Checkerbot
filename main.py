import pyautogui as auto
import time

def getinfo():
    auto.hotkey('alt','tab')
    auto.moveTo(100,60)
    auto.click()
    time.sleep(10)
    auto.hotkey('ctrl','a')
    auto.hotkey('ctrl','c')
    auto.hotkey('alt','tab')
    auto.moveTo(100,180)
    auto.click()
    auto.moveTo(500,400)
    auto.click()
    auto.hotkey('ctrl','a')
    auto.hotkey('ctrl','v')

while True:
    getinfo()
    with open('text','r',encoding="utf-8") as f:
        data=f.read().lower().split()
        for i in data:
            if "score" in i or "result" in i:
                auto.alert(text='SHEHHSH', title='RESULLT OUTT', button='OK')
                exit()
    time.sleep(10)