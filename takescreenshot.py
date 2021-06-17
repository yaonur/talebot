import pyautogui
from pynput.mouse import Listener
import time
import keyboard

def takeScreenShot():
    while True:
        if keyboard.is_pressed(' '):
            x,y=pyautogui.position()
            time.sleep(.5)
            image = pyautogui.screenshot(region=(x, y, 10 , 10 ))

            filename = pyautogui.prompt(text='enter file name', title='', default='')
            print(f'/{filename}X{x}Y{y}.png')
            image.save(f'./{filename}X{x}Y{y}.png')


# def takeScreenShot():
#     while True:
#         if keyboard.is_pressed(' '):
#             x,y=pyautogui.position()
#             time.sleep(.5)
#             image = pyautogui.screenshot(region=(1077 , 447, 10 , 15))
#             filename = pyautogui.prompt(text='enter file name', title='', default='')
#             # print(f'/{filename}X{x}Y{y}.png')
#             image.save(f'{filename}.png')
#

# def on_move(x, y):
#     print('Pointer moved to {0}'.format(
#         (x, y)))
#
#
# def on_click(x, y, button, pressed):
#     time.sleep(.5)
#     image = pyautogui.screenshot(region=(x, y, 10, 10))
#     filename = pyautogui.prompt(text='enter file name', title='', default='')
#     print(f'/{filename}X{x}Y{y}.jpg')
#     image.save(f'./{filename}X{x}Y{y}.jpg')
#     return False
#     #     # Stop listener
#     #     return False
#
#
# def on_scroll(x, y, dx, dy):
#     listener.stop()
  #     # time.sleep(.5)
#     # image = pyautogui.screenshot(region=(x, y, 10, 10))
#     # filename = pyautogui.prompt(text='enter file name', title='', default='')
#     # print(f'/{filename}X{x}Y{y}.jpg')
#     # image.save(f'./{filename}X{x}Y{y}.jpg')
#     # return False
#
#
# # Collect events until released
# with Listener(
#         on_move=on_move,
#         on_scroll=on_scroll,
#         on_click=on_click,
# ) as listener:
#     listener.join()
if __name__ == "__main__":
    takeScreenShot()
