from settings import*
from sprites import*
import button
import os

os.chdir(RESOURCES_DIR)

class Battle:
    def __init__(self):
        self.game_width, self.game_height = LANDSCAPE_WIDTH, LANDSCAPE_HEIGHT
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (50,50)

        self.screen = pygame.display.set_mode((self.game_width,self.game_height))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = True
        self.fps = FPS
        pygame.font.init()
        pygame.mixer.init()

        self.player_team = "You"
        self.enemy_team = "Enemy"

        self.all_sprites = pygame.sprite.Group()
        self.player_unit_sprites = pygame.sprite.Group()
        self.enemy_unit_sprites = pygame.sprite.Group()



        self.knight_card = pygame.image.load("knight-card.png").convert_alpha()
        self.knight_button = button.Button(0,0, self.knight_card,.08)
        self.necromancer_card = pygame.image.load("necromancer-card.png").convert_alpha()
        self.necromancer_button = button.Button(200,0, self.necromancer_card, 0.08)
        self.swordmaster_card = pygame.image.load("swordmaster-card.png").convert_alpha()
        self.swordmaster_button = button.Button(400,0, self.swordmaster_card, 0.08)
        self.archer_card = pygame.image.load("archer-card.png").convert_alpha()
        self.archer_button = button.Button(600,0, self.archer_card, 0.08)
        self.gold = 0


    def new(self):
        
        self.enemy_morale = 100
        self.player_morale = 100
        self.enemy_last_deployed_time = 0

        self.background1 = Static(0, 0, "layers/bg1.png")
        self.background4 = Static(0, 0, "layers/bg2.png")
        self.background2 = Static(0, 0, "layers/bg3.png")
        self.background3 = Static(0, 0, "layers/bg4.png")
        self.background1.transform(1200,600)
        self.background2.transform(1200,600)
        self.background3.transform(1200,600)
        self.background4.transform(1200,600)

        self.all_sprites.add(self.background1, self.background2, self.background3, self.background4)

        self.run()



    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.knight_button.draw(self.screen):
                    self.deploy_unit("left", "knight")
                if self.necromancer_button.draw(self.screen):
                    self.deploy_unit("left", "necromancer")
                if self.archer_button.draw(self.screen):
                    self.deploy_unit('left','archer')
                if self.swordmaster_button.draw(self.screen):
                    self.deploy_unit('left','swordmaster')
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.deploy_unit("left", "archer", )
                if event.key == pygame.K_d:
                    self.deploy_unit("right", "Knight")
                if event.key == pygame.K_w:
                    self.deploy_unit("left", "knight")


        

    def update(self):
        now = pygame.time.get_ticks()
        self.all_sprites.update()
        self.knight_button.draw(self.screen)
        if self.player_morale <= 0:
            self.player_morale = 0
            self.show_game_over_screen()
        elif self.enemy_morale <=0:
            self.enemy_morale = 0
            self.show_game_over_screen(True)
        
        if now - self.enemy_last_deployed_time >= 2500:
            self.gold += 500
            self.enemy_last_deployed_time = now
            self.deploy_unit("right", "knight", 1)


    def show_game_over_screen(self, won=False):
        self.dim_screen = pygame.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0,0,0, 200))
        self.screen.blit(self.dim_screen, (0,0))
        if won:
            self.draw_text("Victory!", 70, GREEN, self.game_width//2, self.game_height//2)
            self.draw_text("press SPACE to exit", 20, GREEN, self.game_width//2, (self.game_height//2)+80)
        else:
            self.draw_text("Defeat!", 70, RED, self.game_width//2, self.game_height//2)
            self.draw_text("press SPACE to exit", 20, RED, self.game_width//2, (self.game_height//2)+80)
        pygame.display.flip()
        self.listen_for_key()

    def listen_for_key(self):
        waiting = True
        while waiting:
            if self.running:
                self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.playing = False
                        self.running = False
                        waiting = False

    def draw_text(self, text, size, color, x, y, anchor="midtop"):
        font = pygame.font.Font("freesansbold.ttf", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if anchor == "center":
            text_rect.center = (x, y)
        else:
            text_rect.midtop = (x, y)
        self.screen.blit(text_surface,text_rect)



    def draw(self):
        if self.playing:
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)
            self.knight_button.draw(self.screen)
            self.necromancer_button.draw(self.screen)
            self.swordmaster_button.draw(self.screen)
            self.archer_button.draw(self.screen)


            font= pygame.font.Font('freesansbold.ttf',32)
            self.my_morale = font.render("My Morale: " + str(self.player_morale), True, GREEN)
            self.screen.blit(self.my_morale, (800,50))
            self.e_morale = font.render("Enemy Morale: " + str(self.enemy_morale), True, RED)
            self.screen.blit(self.e_morale, (800,100))

            gold = font.render("Gold: " + str(self.gold), True, (255,215,0))
            self.screen.blit(gold, (800,150))

            pygame.display.flip()

    def run(self):
        while self.playing:
            self.clock.tick(self.fps)
            self.events()
            self.update()
            self.draw()

    def deploy_unit(self, side, unit_type, slot=1):
        if side == "left":
            if unit_type == 'knight':
                unit = Knight_Infantry(self, 5, self.game_height-80, "Melee", unit_type, self.player_team, side, slot)
            elif unit_type == 'archer':
                unit = Archer_Ranged(self, 5, self.game_height-80, "Ranged", unit_type, self.player_team, side, slot)
            elif unit_type == 'swordmaster':
                unit = Sword_Master(self, 5, self.game_height-80, "Melee", unit_type, self.player_team, side, slot)
            elif unit_type == 'necromancer':
                unit = Necromancer_Ranged(self, 5, self.game_height-80, "Ranged", unit_type, self.player_team, side, slot)



            self.player_unit_sprites.add(unit)
        else:
            unit = Knight_Infantry(self, LANDSCAPE_WIDTH-5, self.game_height-80, "Melee", unit_type, self.enemy_team, side, slot)
            self.enemy_unit_sprites.add(unit)
        self.all_sprites.add(unit)
            



b = Battle()
b.new()
b.run()