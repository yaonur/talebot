import pyautogui
import cv2
import time

coords={'invslot1':(1231,961)}

'''all mouse and key controls here'''
def check_personal(filename, confidence, areaw=12, areah=12, ):
    '''
    :param filename File to search image from
    :param confidence the percentage of the compare precision
    '''

    if position:=pyautogui.locateCenterOnScreen(filename, region=(1620, 800, 285, 145), confidence=confidence):
        return position
    else:
        pass



def check_image(filename, confidence, areaw=12, areah=12,region=None ):
    '''
    :param filename File to search image from
    :param confidence the percentage of the compare precision
    '''
    x = int(filename.rsplit('X')[1].rsplit('Y')[0])
    y = int(filename.rsplit('Y')[1].rsplit('.')[0])
    # if theres region uses that else extracts region from filename
    if region:
        inner_region=region
    else:
        inner_region=(x - 1, y - 1, areaw, areah)
    if  coords:=pyautogui.locateCenterOnScreen(filename, region=inner_region, confidence=confidence):
        return coords
    else:
        return False


def check_slot(filename, confidence, areaw=12, areah=12, ):
    '''
    :param filename File to search image from
    :param confidence the percentage of the compare precision
    '''
    # returns bool and coords
    x = int(filename.rsplit('X')[1].rsplit('Y')[0])
    y = int(filename.rsplit('Y')[1].rsplit('.')[0])
    coords = (x, y)
    if  pyautogui.locateCenterOnScreen(filename, region=(x - 1, y - 1, areaw, areah), confidence=confidence):
        print('found')
        return True, coords
    else:
        print('not found')
        return False, coords


def check_item(filename, confidence, ):
    '''
    :param filename File to search image from
    :param confidence the percentage of the compare precision
    '''

    if position := pyautogui.locateCenterOnScreen(filename, region=(600, 400, 600, 400), confidence=confidence):
        print('found')
        x, y = position
        return x, y
    else:
        print('not found')
        return False


def click(coords):
    pyautogui.moveTo(coords,duration=.1)
    pyautogui.click()
    time.sleep(.2)


def drag(start_coords, end_coords):
    pyautogui.moveTo(start_coords,duration=.1)
    time.sleep(.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_coords,duration=.2)
    pyautogui.mouseUp()
    time.sleep(.1)
    pyautogui.moveTo(916,1050)


def drag_click(start_coords, end_coords):
    pyautogui.moveTo(start_coords,duration=.1)
    time.sleep(.1)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_coords,duration=.2)
    pyautogui.mouseUp()
    time.sleep(.1)
    pyautogui.click()
    time.sleep(.1)
    pyautogui.moveTo(916,1050)


def right_click(coords):
    pyautogui.moveTo(coords)
    pyautogui.rightClick()


def check_invslot(slotnum):
    # checks inv slot returns bool and coords
    if slotnum == 1:
        occupation, sltcoords = check_slot('../../slots/invslot1X1234Y964.png', .9)
        return occupation, sltcoords
    elif slotnum == 2:
        occupation, sltcoords = check_slot('slots/invslot2X1303Y966.png', .9)
        return occupation, sltcoords
    elif slotnum == 3:
        occupation, sltcoords = check_slot('slots/invslot3X1169Y1011.png', .9)
        return occupation, sltcoords
    elif slotnum == 4:
        occupation, sltcoords = check_slot('slots/invslot4X1235Y1011.png', .9)
        return occupation, sltcoords
    elif slotnum == 5:
        occupation, sltcoords = check_slot('../slots/invslot5X1302Y1014.png', .9)
        return occupation, sltcoords

def leave_game():
    print('leaving game')
    pyautogui.click((29,24))
    time.sleep(2)
    pyautogui.click((1671,953))
    time.sleep(1)
    pyautogui.click((1671,953))
    time.sleep(3)
    pyautogui.click((1671,953))
    time.sleep(3)
    pyautogui.click((1671,953))
    time.sleep(1)
    pyautogui.click((1671,953))
