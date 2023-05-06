import pygame
import button
import sys

def loadAndScaleImg(imgName, itemNum):
    imgScale = 10
    img = pygame.image.load(imgName)

    imgWidth = img.get_rect().width
    imgHeight = img.get_rect().height
    img = pygame.transform.scale(img, (imgWidth/imgScale, imgHeight/imgScale))

    inventory[itemNum] = img

images = ["archer-card.png", "knight-card.png", "necromancer-card.png", "pikeman-card.png", "rogue-card.png", "swordmaster-card.png"]
inventory = {}

def gameInventory():
    pygame.init()
    pygame.display.set_caption("Inventory")
    font = pygame.font.SysFont(None, 30)

    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 600

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    for i in range(0, 6):
        itemName = "item" + str(i + 1)
        loadAndScaleImg(images[i], itemName)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

        screen.blit(inventory["item1"], (0, 0))
        screen.blit(inventory["item2"], (250, 0))
        screen.blit(inventory["item3"], (500, 0))
        screen.blit(inventory["item4"], (0, 270))
        screen.blit(inventory["item5"], (250, 270))
        screen.blit(inventory["item6"], (500, 270))

        back_image = pygame.image.load('images/back.png').convert_alpha()
        back_button = button.Button(back_image, 1000, 50)

        if back_button.draw(screen):
            return "map"


        pygame.display.update()
        clock.tick(60)