from modules.mainmenu import mainmenu
from modules.takehero import takehero
from modules.gameend import game_end
from modules.takeskill import takeskill

import time
def main():
    while True:
        mainmenu.main()
        time.sleep(1)
        takehero.main()
        time.sleep(1)
        takeskill.main()
        time.sleep(1)


if __name__ == '__main__':
    main()