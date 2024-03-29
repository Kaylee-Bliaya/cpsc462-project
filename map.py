import pygame
import button
from battle import *
import sys

# ============================================ loadAndScaleImg FUNCTION START ============================================

# function to load an image and scale it to fit the game screen
def loadAndScaleImg(imgName, type):
    if type == 'map':
        imgScale = 3
    elif type == 'btn':
        imgScale = 1
    elif type == 'menu' or type == 'inventory':
        imgScale = 5

    img = pygame.image.load(imgName)

    imgWidth = img.get_rect().width
    imgHeight = img.get_rect().height
    img = pygame.transform.scale(img, (imgWidth/imgScale, imgHeight/imgScale))

    return img

# ============================================ drawBlankButtons FUNCTION START ============================================

# function to draw blank level buttons to represent levels that are
# not yet accessible to the player
def drawBlankButtons(screen, blank):
    screen.blit(blank, (154, 120))
    screen.blit(blank, (200, 279))
    screen.blit(blank, (320, 350))
    screen.blit(blank, (500, 420))
    screen.blit(blank, (750, 470))
    screen.blit(blank, (870, 380))
    screen.blit(blank, (1050, 335))
    screen.blit(blank, (1108, 203))
    screen.blit(blank, (1135, 102))

# ============================================ drawLevelButtons FUNCTION START ============================================

# function to draw the level buttons:
#   check if the previous level has been passed
#       if True, then draw the button for the next playable level
def drawLevelButtons(screen, btn, levelsPassed, currLevel):
    if currLevel - 1 in levelsPassed or currLevel == 1:
        return btn.draw(screen)
    
# ============================================ addLevel FUNCTION START ============================================

# function to add passed levels to the list levelsPassed
def addLevel(levelsPassed, currLevel, levelPassed):
    if (currLevel not in levelsPassed) and levelPassed == "won":
        levelsPassed.append(currLevel)

# set the screen width and height
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# list to record what levels the player has passed
levelsPassed = []

# ============================================ gameMap FUNCTION START ============================================

def gameMap(wonOrLost, level):
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Path of Conquest - Map')
    clock = pygame.time.Clock()

    # load and scale background map image
    map_img = loadAndScaleImg('map_graphics/map.png', 'map')

    # load and scale button images
    btn1_img = loadAndScaleImg('map_graphics/btn1.png', 'btn')
    btn2_img = loadAndScaleImg('map_graphics/btn2.png', 'btn')
    btn3_img = loadAndScaleImg('map_graphics/btn3.png', 'btn')
    btn4_img = loadAndScaleImg('map_graphics/btn4.png', 'btn')
    btn5_img = loadAndScaleImg('map_graphics/btn5.png', 'btn')
    btn6_img = loadAndScaleImg('map_graphics/btn6.png', 'btn')
    btn7_img = loadAndScaleImg('map_graphics/btn7.png', 'btn')
    btn8_img = loadAndScaleImg('map_graphics/btn8.png', 'btn')
    btn9_img = loadAndScaleImg('map_graphics/btn9.png', 'btn')
    btn10_img = loadAndScaleImg('map_graphics/btn10.png', 'btn')
    menuBtn_img = loadAndScaleImg('map_graphics/menu.png', 'menu')
    inventoryBtn_img = loadAndScaleImg('map_graphics/inventory.png', 'inventory')
    blank = loadAndScaleImg('map_graphics/blankBtn.png', 'btn')

    # create button instances
    btn1 = button.Button(btn1_img, 35, 300, 1)
    btn2 = button.Button(btn2_img, 154, 120, 1)
    btn3 = button.Button(btn3_img, 200, 279, 1)
    btn4 = button.Button(btn4_img, 320, 350, 1)
    btn5 = button.Button(btn5_img, 500, 420, 1)
    btn6 = button.Button(btn6_img, 750, 470, 1)
    btn7 = button.Button(btn7_img, 870, 380, 1)
    btn8 = button.Button(btn8_img, 1050, 335, 1)
    btn9 = button.Button(btn9_img, 1108, 203, 1)
    btn10 = button.Button(btn10_img, 1135, 102, 1)
    menuBtn = button.Button(menuBtn_img, 0, 0, 1)
    inventoryBtn = button.Button(inventoryBtn_img, 50, 0, 1)

    run = True
    while run:
        # if the player selects the exit button, quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

        # display the map image on the game screen
        screen.blit(map_img, (0, -200))

        # draw the menu and inventory buttons on the game screen
        if menuBtn.draw(screen):
            run = False
            return "menu"
        if inventoryBtn.draw(screen):
            return "inventory"

        addLevel(levelsPassed, level, wonOrLost)

        # draw the level buttons
        #   * draw the 1st level button and blank buttons for the other levels
        #   * if the current level has been passed, reveal the button for the next
        #       level and add the current level to the list levelsPassed
        drawBlankButtons(screen, blank)

        if drawLevelButtons(screen, btn1, levelsPassed, 1):
            return 1
        if drawLevelButtons(screen, btn2, levelsPassed, 2):
            return 2
        if drawLevelButtons(screen, btn3, levelsPassed, 3):
            return 3
        if drawLevelButtons(screen, btn4, levelsPassed, 4):
            return 4
        if drawLevelButtons(screen, btn5, levelsPassed, 5):
            return 5
        if drawLevelButtons(screen, btn6, levelsPassed, 6):
            return 6
        if drawLevelButtons(screen, btn7, levelsPassed, 7):
            return 7
        if drawLevelButtons(screen, btn8, levelsPassed, 8):
            return 8
        if drawLevelButtons(screen, btn9, levelsPassed, 9):
            return 9
        if drawLevelButtons(screen, btn10, levelsPassed, 10):
            return 10

        pygame.display.update()
        clock.tick(60)