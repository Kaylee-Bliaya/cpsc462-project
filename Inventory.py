import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Inventory")
font = pygame.font.SysFont(None, 30)

inventory = []

items = ["Sword", "Shield", "Potion", "Firestick"]

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                item = random.choice(items)
                inventory.append(item)

    screen.fill(WHITE)

    text = font.render("Inventory: " + ", ".join(inventory), True, BLACK)
    screen.blit(text, [10, 10])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
