# import psutil
import pywinauto
from pywinauto import Desktop
import subprocess


#find the of the program
windows = Desktop(backend="uia").windows()
print([w.window_text() for w in windows])

#set program to front
# app = pywinauto.Application().connect(title="Dota 2")
# app.Dota2.set_focus()

#close program
# app.window().close()

#not working
# pywinauto.application.Application.start(r'F:\\steam\\steamapps\\common\\dota 2 beta\game\\bin\\win64\\dota2.exe')

#start dota with subprocess
fileName = "F:\\steam\\steamapps\\common\\dota 2 beta\\game\\bin\win64\\dota2.exe"
subprocess.call(fileName)
