import pygame, sys
import button
from pygame.locals import *
from pygame import mixer

#bottom_panel = 150
screen_width = 1200 
screen_height = 600 #+ bottom_panel

def gameMenu():
    pygame.init()
    FINAL_ENCOUNTER = 11

    screen = pygame.display.set_mode((screen_width, screen_height)) #- bottom_panel))
    clock = pygame.time.Clock()
            
    #Main menu logic+animation
    pygame.display.set_caption("Main Menu")

    #Background image
    background_image = pygame.image.load("images/background.png").convert_alpha()

    #Draw background
    def draw_background():
        screen.blit(background_image, (0, 0))

    #Draw text
    def draw_text(text, font, color, x, y):
        title = font.render(text, True, color)
        screen.blit(title, (x, y))

    #Font
    font_1 = pygame.font.SysFont("cambria", 70)
    font_2 = pygame.font.SysFont("cambria", 25)

    #Color
    white = (255, 255, 255)

    #Button images
    play_image = pygame.image.load("images/play.png").convert_alpha()
    settings_image = pygame.image.load("images/settings.png").convert_alpha()
    exit_image = pygame.image.load("images/exit.png").convert_alpha()
    music_image = pygame.image.load('images/music.png').convert_alpha()
    back_image = pygame.image.load('images/back.png').convert_alpha()
    decrease_image = pygame.image.load('images/decrease.png').convert_alpha()
    increase_image = pygame.image.load('images/increase.png').convert_alpha()
    bar1_image = pygame.image.load('images/bar1.png').convert_alpha()
    bar2_image = pygame.image.load('images/bar2.png').convert_alpha()
    bar3_image = pygame.image.load('images/bar3.png').convert_alpha()
    bar4_image = pygame.image.load('images/bar4.png').convert_alpha()

    #Button instances
    play_button = button.Button(play_image, 440, 110)
    settings_button = button.Button(settings_image, 440, 245)
    exit_button = button.Button(exit_image, 440, 380)
    music_button = button.Button(music_image, 220, 200)
    back_button = button.Button(back_image, 450, 375)
    decrease_button = button.Button(decrease_image, 430, 220)
    increase_button = button.Button(increase_image, 730, 220)
    bar1_button = button.Button(bar1_image, 490, 220)
    bar2_button = button.Button(bar2_image, 550, 220)
    bar3_button = button.Button(bar3_image, 610, 220)
    bar4_button = button.Button(bar4_image, 670, 220)

    mixer.init()
    mixer.music.load('music/bg_music.mp3')
    pygame.mixer.music.play(-1)

    #Variables
    next_step = False
    menu_state = "main"
    
    #Game loop
    run = True
    while run:
        #draw background
        draw_background()

        if next_step == True:
            #check main
            if menu_state == "main":
                if play_button.draw(screen):
                    from map import gameMap
                    return "map"    #connect to map
                if settings_button.draw(screen):
                    menu_state = "settings"
                if exit_button.draw(screen):
                    run = False
                    return "quit"

            #check settings
            if menu_state == "settings":
                music_button.draw(screen)
                if decrease_button.draw(screen):
                    mixer.music.set_volume(0.0)
                if bar1_button.draw(screen):
                    mixer.music.set_volume(0.2)
                if bar2_button.draw(screen):
                    mixer.music.set_volume(0.4)
                if bar3_button.draw(screen):
                    mixer.music.set_volume(0.6)
                if bar4_button.draw(screen):
                    mixer.music.set_volume(0.8)
                if increase_button.draw(screen):
                    mixer.music.set_volume(1.0)

                if back_button.draw(screen):
                    menu_state = "main"

            if menu_state == "music":
                if back_button.draw(screen):
                    menu_state = "settings"
        else:
            #draw text
            draw_text("PATH TO CONQUEST", font_1, white, 260, 190)
            draw_text("Press SPACE To MAIN MENU", font_2, white, 430, 430)


        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                #press RETURN to go to the next step
                if event.key == pygame.K_SPACE:
                    next_step = True

        #update display
        pygame.display.update()





















