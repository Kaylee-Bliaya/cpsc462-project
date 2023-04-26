import pygame
from sys import exit

class Button():
    def __init__(self, x, y, img):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.img, (self.rect.x, self.rect.y))

        return action

def loadAndScaleBtn(imgName, type):
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

def checkIfLevelPassed(currLevel, levelsPassed):
    if currLevel - 1 in levelsPassed:
        return True
    return False

def addLevel(currLevel, levelsPassed):
    if currLevel not in levelsPassed:
        levelsPassed.append(currLevel)
    return levelsPassed

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Path of Conquest')
clock = pygame.time.Clock()

# load and scale background map image
image = loadAndScaleBtn('map_graphics/map.png', 'map')

# load and scale button images
btn1_img = loadAndScaleBtn('map_graphics/btn1.png', 'btn')
btn2_img = loadAndScaleBtn('map_graphics/btn2.png', 'btn')
btn3_img = loadAndScaleBtn('map_graphics/btn3.png', 'btn')
btn4_img = loadAndScaleBtn('map_graphics/btn4.png', 'btn')
btn5_img = loadAndScaleBtn('map_graphics/btn5.png', 'btn')
btn6_img = loadAndScaleBtn('map_graphics/btn6.png', 'btn')
btn7_img = loadAndScaleBtn('map_graphics/btn7.png', 'btn')
btn8_img = loadAndScaleBtn('map_graphics/btn8.png', 'btn')
btn9_img = loadAndScaleBtn('map_graphics/btn9.png', 'btn')
btn10_img = loadAndScaleBtn('map_graphics/btn10.png', 'btn')
menuBtn_img = loadAndScaleBtn('map_graphics/menu.png', 'menu')
inventoryBtn_img = loadAndScaleBtn('map_graphics/inventory.png', 'inventory')

# create button instances
btn1 = Button(35, 300, btn1_img)
btn2 = Button(154, 120, btn2_img)
btn3 = Button(200, 279, btn3_img)
btn4 = Button(320, 350, btn4_img)
btn5 = Button(500, 420, btn5_img)
btn6 = Button(750, 470, btn6_img)
btn7 = Button(870, 380, btn7_img)
btn8 = Button(1050, 335, btn8_img)
btn9 = Button(1108, 203, btn9_img)
btn10 = Button(1135, 102, btn10_img)
menuBtn = Button(0, 0, menuBtn_img)
inventoryBtn = Button(50, 0, inventoryBtn_img)

levelsPassed = []

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(image, (0, -200))

    if menuBtn.draw():
        print('menu')
    if inventoryBtn.draw():
        print('inventory')

    if btn1.draw():
        print('level 1')
        addLevel(1, levelsPassed)
    if btn2.draw() and checkIfLevelPassed(2, levelsPassed):
        print('level 2')
        addLevel(2, levelsPassed)
    if btn3.draw() and checkIfLevelPassed(3, levelsPassed):
        print('level 3')
        addLevel(3, levelsPassed)
    if btn4.draw() and checkIfLevelPassed(4, levelsPassed):
        print('level 4')
        addLevel(4, levelsPassed)
    if btn5.draw() and checkIfLevelPassed(5, levelsPassed):
        print('level 5')
        addLevel(5, levelsPassed)
    if btn6.draw() and checkIfLevelPassed(6, levelsPassed):
        print('level 6')
        addLevel(6, levelsPassed)
    if btn7.draw() and checkIfLevelPassed(7, levelsPassed):
        print('level 7')
        addLevel(7, levelsPassed)
    if btn8.draw() and checkIfLevelPassed(8, levelsPassed):
        print('level 8')
        addLevel(8, levelsPassed)
    if btn9.draw() and checkIfLevelPassed(9, levelsPassed):
        print('level 9')
        addLevel(9, levelsPassed)
    if btn10.draw() and checkIfLevelPassed(10, levelsPassed):
        print('level 10')
        addLevel(10, levelsPassed)

    pygame.display.update()
    clock.tick(60)