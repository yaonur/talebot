import pyautogui
import time
import globalfunctions as gf


def check_main_menu():
    '''
    gonna check if in main menu and enter game
    '''
    number_of_try=0
    while True:
        number_of_try+=1
        if arcade := gf.check_image('images/arcadeonlineX1107Y30.png', .95):
            print('arcade')
            gf.click(arcade)
            time.sleep(.4)
        if library := gf.check_image('images/library20bt40X617Y83.png', .99,41,21):
            print('library')
            gf.click(library)
            time.sleep(.4)
        if tale := gf.check_image('images/taleX866Y390.png', .95):
            print('tale')
            gf.click(tale)
            time.sleep(.9)
        if createlobby := gf.check_image('images/createlobbyX1491Y548.png', .9, 12, 100):
            print('blue create lobby')
            gf.click(createlobby)
            time.sleep(.4)
        if createlobby := gf.check_image('images/createlooby2X710Y639.png', .9):
            gf.click(createlobby)
            time.sleep(.4)
            pyautogui.move(0, 30)
            pyautogui.click()
            time.sleep(.4)
            pyautogui.press('o')
            time.sleep(.8)
            if gf.check_image('images/loobypassX700Y664.png', .9):
                if createlobby := gf.check_image('images/createloby3X995Y833.png', .9):
                    gf.click(createlobby)
                time.sleep(2)
        if alreadycreated := gf.check_image('images/alreadycreatedX1557Y1032.png', .9):
            gf.click(alreadycreated)
            time.sleep(.4)
        if stargame := gf.check_image('images/startgameX1675Y1037.png', .9):
            gf.click(stargame)
            time.sleep(.9)
        # if accept := gf.check_image('images/acceptX989Y521.png', .9):
        #     gf.click(accept)
        #     time.sleep(.6)
        if number_of_try > 4:
            break


if __name__ == '__main__':
    check_main_menu()
