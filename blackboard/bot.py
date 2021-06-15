import time
import threading

statebot = 'mainmenu'


def fightinCreeps():
    while True:
        if statebot=='creep':
            print('fighting normal creeps')
            time.sleep(1)
        else:
            break

def fightingBoss():
    while True:
        if statebot=='boss':
            print('fighting boss')
            time.sleep(1)
        else:
            break


def botcheckstate():
    while True:

        if (statebot == 'boss'):
            fightingBoss()
            print('boss')

        if (statebot == 'creep'):
            fightinCreeps()
            print('creep')
        else:
            print('mainmenu')
        time.sleep(1)


def botsetstate(state):
    global statebot
    statebot = state
    print(statebot)


tBot = threading.Thread(target=botcheckstate)
tBot.start()
print('bot is imported')
