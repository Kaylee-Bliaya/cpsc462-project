# bg_music
from mainMenu import *
from map import *
from settings import *

os.chdir(RESOURCES_DIR)

SCENE_MENU = "menu"
SCENE_MAP = "map"
SCENE_PLAY = "play"

def main():
    scene = SCENE_MENU
    BEEN_TO_MAP = False

    while True:
        if scene == SCENE_MENU:
            scene = gameMenu(BEEN_TO_MAP)
        if scene == SCENE_MAP:
            scene = gameMap()
            BEEN_TO_MAP = True
        if scene == "quit":
            pygame.quit()
            quit()

main()