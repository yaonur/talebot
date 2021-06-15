import threading
import keyboard
import time
import bot
import asyncio


def checkkey():
    while True:
        # print('loop is running')
        if keyboard.is_pressed('q'):
            bot.botsetstate('boss')
            # print('q is pressed')
        if keyboard.is_pressed('c'):
            bot.botsetstate('creep')
            # print('c is pressed')
        else:
            pass
            # print('no state')
        time.sleep(.5)


tCheckkey = threading.Thread(target=checkkey)
tCheckkey.start()
# bot.tBot.start()