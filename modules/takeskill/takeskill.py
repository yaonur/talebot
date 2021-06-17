import globalfunctions as gf
import pyautogui
import time
from modules.openshop import openshop
import os
skill_points=0
def main():
    os.chdir(r'F:/python/talebot')
    global skill_points
    final=0
    # openshop.main()
    opentome('modules/takeskill/tomes/redtomeX1878Y814.png')
    final=skill_points*3
    opentome('modules/takeskill/tomes/yellowtomeX1685Y812.png')
    final+=skill_points*2
    opentome('modules/takeskill/tomes/orangetomeX1635Y847.png')
    final+=skill_points
    opentome('modules/takeskill/tomes/purpletomeX1639Y813.png')
    if final<27:
        gf.leave_game()
    # take_skill()
def opentome(filename):
    while tome:= gf.check_personal(filename,.8):
        gf.drag_click(tome,(1234,964))
        gf.drag((1234,964),tome)
        time.sleep(.1)
        take_skill()
        time.sleep(.1)


def take_skill():
    global skill_points
    skill_points=0
    if skill:= gf.check_personal('modules/takeskill/skills/blood.png',.8):
        gf.drag_click(skill,(1234,964))
        skill_points+=6
    if skill:= gf.check_personal('modules/takeskill/skills/life.png',.8):
        gf.drag_click(skill,(1234,964))
        skill_points += 5
    if skill:= gf.check_personal('modules/takeskill/skills/bleeding.png',.8):
        gf.drag_click(skill,(1234,964))
        skill_points+=3


skill_points += 6
if __name__ == '__main__':
    main()
