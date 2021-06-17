from pywinauto import Desktop
import pywinauto
import pyautogui
import subprocess
import time


# find the of the program

def check_process():
    windows = Desktop(backend="uia").windows()
    dota = False
    tale=False

    for w in windows:
        task = w.window_text()
        if task == 'Dota 2':
            print('found dota')
            dota = True
    if dota == False:
        try:
            dota = 'F:/steam/steamapps/common/dota 2 beta/game/bin/win64/dota2.exe'
            subprocess.Popen(dota)
            time.sleep(5)
        except:
            pass
    for w in windows:
        task = w.window_text()
        if task == 'TaleOfSourgeAFK_SSSSSSSSS_FarmByHands':
            print('found tale')
            tale=True

        # else:
    if tale==False:
        try:
            filename = 'C:/Users/yaonur/Downloads/Dota2beta5/Dota2Bot_protected.exe'
            subprocess.Popen(filename)
            time.sleep(5)
        except:
            pass
    print('looking for err')

    if pyautogui.locateCenterOnScreen('fatal3.png',region=(200,200,1000,600),confidence=.8):
        print('v8 found')
        try:
            app = pywinauto.Application().connect(title="Dota 2")
            app.window().close()
            time.sleep(3)

        except:
            pass
    print('looking for v8')
    if pyautogui.locateCenterOnScreen('error.png', region=(300, 1000, 1600,79),confidence=.8):
        print('err found')
        try:
            app = pywinauto.Application().connect(title="Dota 2")
            app.window().close()
        except:
            pass
    time.sleep(8)
    check_process()


check_process()
