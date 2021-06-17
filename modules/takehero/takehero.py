import globalfunctions as gf
import time
import pyautogui
import os

count = 0


def main():

    os.chdir(r'F:/python/talebot')
    choose_hero()
    print ('count')
    if count == 5:
        return False
    set_difficulty()

def set_difficulty():


    for i in range(9):
        gf.click((1645, 594))
        time.sleep(.3)
    gf.click((1739,290))
    time.sleep(.9)
    gf.click((1739,290))
    time.sleep(.8)
    gf.click((1670,374))
    time.sleep(.4)
    gf.click((884, 765))


def choose_hero():
    global count
    if count == 5:
        gf.leave_game()
    if hero := gf.check_image('modules/takehero/images/strX176Y635.png', .9,850,55):
        gf.click(hero)
        print('hero  found')
        time.sleep(.5)
        count = 0
        pass
    else:
        gf.click((561, 771))
        time.sleep(.8)
        count += 1
        choose_hero()

if __name__ == '__main__':
    main()
