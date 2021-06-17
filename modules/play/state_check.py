import pyautogui
import time
import threading
import positions
def start_state_control():
    tskill_level=threading.Thread(target=skill_level)
    tskill_level.start()
    ttreasure_tome=threading.Thread(target=treasure_tome)
    ttreasure_tome.start()
    ttreasure_screen=threading.Thread(target=treasure_screen)
    ttreasure_screen.start()
    tis_dead=threading.Thread(target=is_dead)
    tis_dead.start()
    tis_boss=threading.Thread(target=is_boss)
    tis_boss.start()
    tskill_points=threading.Thread(target=skill_points)
    tskill_points.start()
    tset_boss=threading.Thread(target=set_boss)
    tset_boss.start()
    tpersonal_boss=threading.Thread(target=personel_boss)
    tpersonal_boss.start()
    tset_boss=threading.Thread(target=set_boss)
    tset_boss.start()
    tskill_points=threading.Thread(target=skill_points)
    tskill_points.start()
    titem_ground=threading.Thread(target=item_ground)
    titem_ground.start()
    titem_inventory=threading.Thread(target=item_inventory)
    titem_inventory.start()
    pass

def skill_level():

    pass

def treasure_tome():
    # while True:
    personel_pos_lvl3=positions.calculate_offset('modules/play/images/books/level3bookX1185Y1009.png','personal_inv',.9)
    # personel_pos_lvl3=positions.personel_inventory_coords()
    # positions.loop_coords(personel_pos_lvl3,.3)
    pass

def treasure_screen():
    pass

def is_dead():
    pass

def is_boss():
    pass

def skill_points():
    pass

def set_boss():
    pass

def personel():
    pass

def personel_boss():
    pass

def skill_points():
    pass

def item_ground():
    pass

def item_inventory():
    pass

if __name__ == '__main__':
    start_state_control()