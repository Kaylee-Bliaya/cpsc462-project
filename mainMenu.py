import pygame, sys
import button
from pygame.locals import *
from pygame import mixer

screen_width = 1200 
screen_height = 600 

def gameMenu(BEEN_TO_MAP):
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height)) 
            
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
    black = (0, 0, 0)

    #Button images
    play_image = pygame.image.load("images/play.png").convert_alpha()
    settings_image = pygame.image.load("images/settings.png").convert_alpha()
    exit_image = pygame.image.load("images/exit.png").convert_alpha()
    music_image = pygame.image.load('images/music.png').convert_alpha()
    back_image = pygame.image.load('images/back.png').convert_alpha()
    decrease_image = pygame.image.load('images/decrease.png').convert_alpha()
    increase_image = pygame.image.load('images/increase.png').convert_alpha()
    bar_image = pygame.image.load('images/bar.png').convert_alpha()

    #Button instances
    play_button = button.Button(play_image, 510, 130, 1)
    settings_button = button.Button(settings_image, 510, 265, 1)
    exit_button = button.Button(exit_image, 510, 400, 1)
    music_button = button.Button(music_image, 300, 220, 1)
    back_button = button.Button(back_image, 510, 375, 1)
    decrease_button = button.Button(decrease_image, 460, 230, 1)
    increase_button = button.Button(increase_image, 700, 230, 1)

    mixer.init()
    mixer.music.load('music/bg_music.mp3')
    pygame.mixer.music.play(-1)

    #Variables
    next_step = False
    menu_state = "main"
    bar_x_offset = 0

    #Draw a volume bar
    def draw_volume_bar(x,y):
        screen.blit(bar_image, (x+bar_x_offset, y))

    #Draw a black rectangle
    def draw_black_rect(x, y, width, height):
        pygame.draw.rect(screen, black, (x, y, width, height))
    
    #Game loop
    run = True
    while run:
        #draw background
        draw_background()

        if next_step == True or BEEN_TO_MAP == True:
            #check main
            if menu_state == "main":
                if play_button.draw(screen):
                    return "map"    #connect to map
                if settings_button.draw(screen):
                    menu_state = "settings"
                if exit_button.draw(screen):
                    run = False
                    return "quit"

            #check settings
            if menu_state == "settings":
                music_button.draw(screen)
                draw_black_rect(500, 230, 200, 40)
                draw_volume_bar(700,230)

                if decrease_button.draw(screen):
                    current_volume = mixer.music.get_volume()
                    if current_volume > 0.0:
                        mixer.music.set_volume(max(0.0, current_volume-0.2))
                        bar_x_offset -= 40
                    
                if increase_button.draw(screen):
                    current_volume = mixer.music.get_volume()
                    if current_volume < 1.0:
                        mixer.music.set_volume(min(1.0, current_volume+0.2))
                        bar_x_offset +=40

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
                return "quit"
            
            if event.type == pygame.KEYDOWN:
                #press RETURN to go to the next step
                if event.key == pygame.K_SPACE:
                    next_step = True

        #update display
        pygame.display.update()