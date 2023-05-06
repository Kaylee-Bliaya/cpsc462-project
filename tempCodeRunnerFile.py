# bg_music
from mainMenu import *
from map import *
from Inventory import *
from settings import *

os.chdir(RESOURCES_DIR)

SCENE_MENU = "menu"
SCENE_MAP = "map"
SCENE_INVENTORY = "inventory"

def main():
    scene = SCENE_MENU
    BEEN_TO_MAP = False
    wonOrLost = ""
    level = 1

    while True:
        if scene == SCENE_MENU:
            scene = gameMenu(BEEN_TO_MAP)
        if scene == SCENE_MAP:
            scene = gameMap(wonOrLost, level)
            BEEN_TO_MAP = True
        if scene == SCENE_INVENTORY:
            scene = gameInventory()
        if type(scene) == int:
            (wonOrLost, level) = gamePlay(scene)
            scene = SCENE_MAP
        if scene == "quit":
            pygame.quit()
            quit()

main()