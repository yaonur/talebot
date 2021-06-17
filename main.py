from modules.mainmenu import mainmenu
from modules.takehero import takehero
from modules.gameend import game_end
from modules.takeskill import takeskill
from modules.openshop  import openshop
import globalfunctions as gf
import time


def main():
    while True:
        check_main_menu()
        check_ingame()
        check_hero_select()
        time.sleep(2)


def check_main_menu():
    check_loading()
    if gf.check_image('images/leavegameX1744Y959.png', .9) or gf.check_image('images/discX1632Y957.png',.9) :
        print('leave game')
        gf.leave_game()
        return
    if gf.check_image('images/mainX1219Y1036.png', .9) or gf.check_image('images/mainbluestartX1693Y1030.png',
                                                                         .9) or gf.check_image(
        'images/mainloadingX1848Y1027.png', .9) or gf.check_image('images/mainacceptX969Y519.png',
                                                                  .9) or gf.check_image(
        'images/maingreencreateX1013Y833.png', .9):
        print('in main menu')
        mainmenu.main()
        pass
    return


def check_ingame():
    if gf.check_image('images/ingameX1360Y1034.png', .9):
        pass
    else:
        return
    if not gf.check_image('images/ingamewareX1773Y596.png',.9):
        openshop.main()
        return
    if gf.check_image('images/ingameskillslotX890Y962.png', .9) or gf.check_image('images/ingameredX1884Y815.png', .9):
        print('ingame start')
        takeskill.main()
        pass
    else:
        print('ingame late')
    return


def check_hero_select():
    if gf.check_image('images/heroselectX594Y767.png', .9):
        print('hero selection')
        takehero.main()
        pass
    return



def check_loading():
    if gf.check_image('images/loading1X1024Y635.png',.9) or gf.check_image('images/mainloadingX1848Y1027.png',.9):
        print('loading')
        time.sleep(5)
        pass


if __name__ == '__main__':
    main()
