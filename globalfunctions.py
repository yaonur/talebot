import pyautogui
import cv2


def check_image(filename, confidence):
    '''
    :param filename File to search image from
    :param confidence the percentage of the compare precision
    '''
    x = int(filename.rsplit('X')[1].rsplit('Y')[0])
    y = int(filename.rsplit('Y')[1].rsplit('.')[0])
    if pyautogui.locateCenterOnScreen(filename, region=(x - 1, y - 1, 12, 12), confidence=confidence):
        print('found')
        return x,y
    else:
        print('not found')
        return False


def click(coords):
    pyautogui.moveTo(coords)
    pyautogui.click()

def drag(start_coords,end_coords):
    pyautogui.moveTo(start_coords)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_coords)
    pyautogui.mouseUp()

def drag_click(start_coords,end_coords):
    pyautogui.moveTo(start_coords)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_coords)
    pyautogui.mouseUp()
    pyautogui.click()

def right_click(coords):
    pyautogui.move(coords)
    pyautogui.rightClick()