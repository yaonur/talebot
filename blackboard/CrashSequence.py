# import psutil
import pywinauto
from pywinauto import Desktop
import subprocess
import time

# find the of the program
windows = Desktop(backend="uia").windows()
print([w.window_text() for w in windows])

for w in windows:
    print(w.window_text())
    task= w.window_text()
    if task == 'TaleOfSourgeAFK_SSSSSSSSS_FarmByHands':
        print('found')
print('all finished')
# for w in windows:
#     print(w.window_text())
#     if w.window_text() == 'TaleOfSourgeAFK_SSSSSSSSS_FarmByHands':
#         print('found')
#         time.sleep(60)
#         break
    # else:
    #      print('not found')
    #      filename='C:/Users/yaonur/Downloads/Dota2beta5/Dota2Bot_protected.exe'
    #      subprocess.call(filename)

# set program to front
# app = pywinauto.Application().connect(title="Dota 2")
# app.Dota2.set_focus()

# close program
# app.window().close()

# not working
# pywinauto.application.Application.start(r'F:\\steam\\steamapps\\common\\dota 2 beta\game\\bin\\win64\\dota2.exe')

# start dota with subprocess
# fileName = "F:\\steam\\steamapps\\common\\dota 2 beta\\game\\bin\win64\\dota2.exe"
# subprocess.call(fileName)
