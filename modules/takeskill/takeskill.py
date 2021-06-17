import globalfunctions as gf
import pyautogui
import time
from modules.openshop import openshop
import os

skill_points = 0


def main():
    os.chdir(r'F:/python/talebot')
    global skill_points
    final = 0
    time.sleep(3)
    if not gf.check_image('modules/takeskill/lordupX106Y435.png', .7) or gf.check_image(
            'modules/takeskill/takeskillbossX106Y560.png', .9):
        print('lord challange screen is off returning')
        return

    openshop.main()
    opentome('modules/takeskill/tomes/redtomeX1878Y814.png')
    print('found red tome')
    final = skill_points * 3
    opentome('modules/takeskill/tomes/yellowtomeX1685Y812.png')
    print('found yellow tome')
    final += skill_points * 2
    opentome('modules/takeskill/tomes/orangetomeX1635Y847.png')
    print('found orange tome')
    final += skill_points
    opentome('modules/takeskill/tomes/purpletomeX1639Y813.png')
    print(final)
    print(' skill points')
    if final < 27:
        gf.leave_game()
    # take_skill()
    return


def opentome(filename):
    while tome := gf.check_personal(filename, .8):
        gf.drag_click(tome, (1234, 964))
        gf.drag((1234, 964), tome)
        time.sleep(.1)
        take_skill()
        time.sleep(.1)


def take_skill():
    global skill_points
    skill_points = 0
    if skill := gf.check_personal('modules/takeskill/skills/blood.png', .8):
        gf.drag_click(skill, (1234, 964))
        skill_points += 6
    if skill := gf.check_personal('modules/takeskill/skills/life.png', .8):
        gf.drag_click(skill, (1234, 964))
        skill_points += 5
    if skill := gf.check_personal('modules/takeskill/skills/bleeding.png', .8):
        gf.drag_click(skill, (1234, 964))
        skill_points += 3


skill_points += 6
if __name__ == '__main__':
    main()
