# bg_music
from mainMenu import *
from map import *

SCENE_MENU = "menu"
SCENE_MAP = "map"

def main():
    scene = SCENE_MENU

    while True:
        if scene == SCENE_MENU:
            scene = gameMenu()
        if scene == SCENE_MAP:
            scene = gameMap()
        if scene == "quit":
            pygame.quit()
            quit()

main()