import globalfunctions as gf
import pyautogui
import time
import os



def main():
    os.chdir(r'F:/python/talebot')

    if settle := gf.check_image('modules/gameend/images/settlementinterfaceX421Y27.png', .9):
        if close := gf.check_image('modules/gameend/images/closeinterX1019Y975.png', .9):
            gf.click(close)
            print('main close')
            time.sleep(.3)
            pass
        else:
            gf.click(settle)
            print('settle')
            pass
        sell_items()
        gf.click(settle)
        time.sleep(.4)
        if leave := gf.check_image('modules/gameend/images/leaveX830Y975.png', .9):
            gf.click(leave)
            time.sleep(1)
            pass


    if leaveout:=gf.check_image('modules/gameend/images/leaveafteringameX1655Y957.png',.9):
        gf.click(leaveout)

    return


def sell_items():
    openarch()

    sell('modules/gameend/images/orange.png', .97)
    sell('modules/gameend/images/yellow.png', .97)


def sell(filename, confidence):
    print('in sell function')
    if items := pyautogui.locateAllOnScreen(filename, region=(1071, 390, 300, 290), confidence=confidence):
        for item in items:
            print('item found')
            gf.click(pyautogui.center(item))
            time.sleep(.1)
        pass
    else:
        print('no itemfound')
        pass
    gf.click((1174,709))
    time.sleep(1)
    gf.click((1010,570))
    time.sleep(.4)



def openarch():
    if gf.check_image('modules/gameend/images/archivescreenX952Y273.png', .9, 22, 22):
        print('archive screen found')
        pass
    else:
        print('no archive clicking')
        gf.click((790, 966))
        time.sleep(1)
        print('moving')
        pass
    print('finished')
    if disintegrate := gf.check_image('modules/gameend/images/disintegrateX1104Y709.png', .9):
        gf.click(disintegrate)
        time.sleep(.7)
        pass


if __name__ == '__main__':
    main()
