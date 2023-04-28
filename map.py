import pygame
import button

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

# function to check if the previous level has been passed
def checkIfLevelPassed(currLevel, levelsPassed):
    if currLevel - 1 in levelsPassed:
        return True
    return False

# function to add the passed level to a list called levelsPassed
# if the level has been passed previously, don't add it to the list
def addLevel(currLevel, levelsPassed):
    if currLevel not in levelsPassed:
        levelsPassed.append(currLevel)
    return levelsPassed

# set the screen width and height
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# ============================================ gameMap() FUNCTION START ============================================

def gameMap():
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

    # create button instances
    btn1 = button.Button(btn1_img, 35, 300)
    btn2 = button.Button(btn2_img, 154, 120)
    btn3 = button.Button(btn3_img, 200, 279)
    btn4 = button.Button(btn4_img, 320, 350)
    btn5 = button.Button(btn5_img, 500, 420)
    btn6 = button.Button(btn6_img, 750, 470)
    btn7 = button.Button(btn7_img, 870, 380)
    btn8 = button.Button(btn8_img, 1050, 335)
    btn9 = button.Button(btn9_img, 1108, 203)
    btn10 = button.Button(btn10_img, 1135, 102)
    menuBtn = button.Button(menuBtn_img, 0, 0)
    inventoryBtn = button.Button(inventoryBtn_img, 50, 0)

    # list to record what levels the player has passed
    levelsPassed = []

    run = True
    while run:
        # if the player selects the exit button, quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # display the map image on the game screen
        screen.blit(map_img, (0, -200))

        # draw the menu and inventory buttons on the game screen
        if menuBtn.draw(screen):
            run = False
            return "menu"
        if inventoryBtn.draw(screen):
            print('go to inventory')

        # draw the level buttons
        #   * if the level button is drawn and the previous level has been passed
        #       allow the player to select the next level button
        #   * when a level has been passed add the level to the list levelsPassed
        if btn1.draw(screen):
            print('level 1')
            addLevel(1, levelsPassed)
        if btn2.draw(screen) and checkIfLevelPassed(2, levelsPassed):
            print('level 2')
            addLevel(2, levelsPassed)
        if btn3.draw(screen) and checkIfLevelPassed(3, levelsPassed):
            print('level 3')
            addLevel(3, levelsPassed)
        if btn4.draw(screen) and checkIfLevelPassed(4, levelsPassed):
            print('level 4')
            addLevel(4, levelsPassed)
        if btn5.draw(screen) and checkIfLevelPassed(5, levelsPassed):
            print('level 5')
            addLevel(5, levelsPassed)
        if btn6.draw(screen) and checkIfLevelPassed(6, levelsPassed):
            print('level 6')
            addLevel(6, levelsPassed)
        if btn7.draw(screen) and checkIfLevelPassed(7, levelsPassed):
            print('level 7')
            addLevel(7, levelsPassed)
        if btn8.draw(screen) and checkIfLevelPassed(8, levelsPassed):
            print('level 8')
            addLevel(8, levelsPassed)
        if btn9.draw(screen) and checkIfLevelPassed(9, levelsPassed):
            print('level 9')
            addLevel(9, levelsPassed)
        if btn10.draw(screen) and checkIfLevelPassed(10, levelsPassed):
            print('level 10')
            addLevel(10, levelsPassed)

        pygame.display.update()
        clock.tick(60)