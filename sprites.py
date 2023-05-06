import pygame


class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame, width, height, scale, colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey(colour)

		return image

class Static(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x,y
    
    def transform(self, x,y):
        self.image = pygame.transform.scale(self.image,(x,y))

        
class Unit(pygame.sprite.Sprite):
    def __init__(self, game, x, y, unit_class, unit_type, unit_team, side, slot, walk_frames,
                 attack_frames, damage_frame, attacking_range, health, attack, defense, walking_acc, walk_width, attack_width,height):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

        self.unit_class = unit_class
        self.unit_type = unit_type
        self.unit_team = unit_team

        self.side = side
        self.slot = slot
        self.walking_animation_length = walk_frames
        self.attacking_animation_length = attack_frames

        self.walk_width = walk_width
        self.attack_width = attack_width
        self.height = height

        self.health = health
        self.attack = attack
        self.defense = defense
        self.walking_acc = walking_acc

        self.attacking = False
        self.attacking_range = attacking_range
        self.position_x, self.position_y = x, y


        self.last_update = 0
        self.current_frame = 0
        self.damage_frame = damage_frame
        self.load_animations()

        self.image = self.walking_animations[0]
        self.rect = self.image.get_rect()
        if self.side == "left":
             self.enemy_sprites = self.game.enemy_unit_sprites
             self.rect.left, self.rect.centery = self.position_x,self.position_y
        else:
            self.enemy_sprites = self.game.player_unit_sprites
            self.rect.left, self.rect.centery = self.position_x,self.position_y
        
        self.health_bar_front = UnitHealthBar(self.rect.centerx,self.rect.top, "health_bar_front.png", self.game, master=self)
        self.health_bar_back = UnitHealthBar(self.rect.centerx,self.rect.top, "health_bar_back.png", self.game, master=self, front = False)

        self.game.all_sprites.add(self.health_bar_back)
        self.game.all_sprites.add(self.health_bar_front)


    def get_animation(self,sprite_sheet, master_list, animation_steps, width, height):
        step_counter = 0
        for step_counter in range(animation_steps):
            master_list.append(sprite_sheet.get_image(step_counter, width, height, 1.8,'black'))
            step_counter += 1




    def load_animations(self):
        #using the spritesheet and get_animation function to cut up the sprite sheet and load each frame into a list
        pre_walk_sprite_sheet = pygame.image.load("{}_walking.png".format(self.unit_type)).convert_alpha()
        walk_sprite_sheet = SpriteSheet(pre_walk_sprite_sheet)
        self.walking_animations = []
        self.get_animation(walk_sprite_sheet, self.walking_animations, self.walking_animation_length, self.walk_width, self.height)
        print(self.walking_animations)
        pre_attack_sprite_sheet = pygame.image.load("{}_attacking.png".format(self.unit_type)).convert_alpha()
        attack_sprite_sheet = SpriteSheet(pre_attack_sprite_sheet)
        self.attacking_animations = []
        self.get_animation(attack_sprite_sheet, self.attacking_animations, self.attacking_animation_length, self.attack_width, self.height)

        #mirroring each animation frame if it is an enemy unit (coming from the right)
        if self.side == "right":
            for i in range(len(self.walking_animations)):
                  frame = self.walking_animations[i]
                  self.walking_animations[i] = pygame.transform.flip(frame, True, False).convert_alpha()
            for i in range(len(self.attacking_animations)):
                  frame = self.attacking_animations[i]
                  self.attacking_animations[i] = pygame.transform.flip(frame, True, False).convert_alpha()
                  

    def update(self):
        self.animate()

        self.enemy_sprites_same_slot = pygame.sprite.Group()
        for enemy_sprite in self.enemy_sprites:
             if self.slot == enemy_sprite.slot:
                  self.enemy_sprites_same_slot.add(enemy_sprite)
        if not self.attacking:
            for enemy_unit in self.enemy_sprites_same_slot:
                if abs(self.rect.left - enemy_unit.rect.left) <= self.attacking_range:
                     self.attacking = True
                     self.current_frame = 0
                     break

            if self.side == "left":
                self.position_x += self.walking_acc
                self.rect.left = self.position_x
                if self.rect.centerx >= self.game.game_width + 50:
                    self.kill()
                    self.health_bar_front.kill()
                    self.health_bar_back.kill()
                    self.game.enemy_morale -= self.health//10
                    print(self.game.enemy_morale)
            else:
                self.position_x -= self.walking_acc
                self.rect.right = self.position_x

                if self.rect.centerx <= -50:
                    self.kill()
                    self.health_bar_front.kill()
                    self.health_bar_back.kill()
                    self.game.player_morale -= self.health//10
                    print(self.game.player_morale)
        else:
            if self.current_frame == self.damage_frame:
                enemy_collision = pygame.sprite.spritecollide(self,self.enemy_sprites_same_slot, False)
                if enemy_collision:
                     closest_enemy = enemy_collision[0]
                     damage_dealt = (self.attack+2)/(closest_enemy.defense+2)
                     closest_enemy.got_hit(damage_dealt)
                else:
                    self.attacking = False

        

    def animate(self):
         now = pygame.time.get_ticks()
         if now - self.last_update > 100:
            self.last_update = now

            if not self.attacking:
                self.current_frame = (self.current_frame+1)%(len(self.walking_animations))
                self.image = self.walking_animations[self.current_frame]
            else:
                self.current_frame = (self.current_frame+1)%(len(self.attacking_animations))
                self.image = self.attacking_animations[self.current_frame]
                self.rect = self.image.get_rect()
                if self.side == "left":
                     self.rect.left = self.position_x
                     self.rect.centery = self.position_y
                else:
                     self.rect.right = self.position_x
                     self.rect.centery = self.position_y

    def got_hit(self, damage):
         self.health -= damage
         if self.health <= 0:
              self.health = 0
              self.kill()
              self.health_bar_front.kill()
              self.health_bar_back.kill()
                 
        


class Knight_Infantry(Unit):
        def __init__(self, game, x, y, unit_class, unit_type, unit_team, side, slot):
            Unit.__init__(self, game, x, y, unit_class, unit_type, unit_team, side, slot, walk_frames = 8, attack_frames = 22, damage_frame = 11,
                           attacking_range=120, health = 100, attack = 25,
                           defense = 1, walking_acc=2, walk_width= 96, attack_width= 144,height=64)
            
class Archer_Ranged(Unit):
        def __init__(self, game, x, y, unit_class, unit_type, unit_team, side, slot):
            Unit.__init__(self, game, x, y, unit_class, unit_type, unit_team, side, slot, walk_frames = 8, attack_frames = 14, damage_frame = 13,
                           attacking_range=300, health = 50, attack = 15,
                           defense = 1, walking_acc=1, walk_width= 128, attack_width= 180,height=128)
            
class Sword_Master(Unit):
        def __init__(self, game, x, y, unit_class, unit_type, unit_team, side, slot):
            Unit.__init__(self, game, x, y, unit_class, unit_type, unit_team, side, slot, walk_frames = 8, attack_frames = 7, damage_frame = 5,
                            attacking_range=120, health = 100, attack = 30,
                            defense = 1, walking_acc=3, walk_width= 162, attack_width= 162,height=162)
            
class Necromancer_Ranged(Unit):
        def __init__(self, game, x, y, unit_class, unit_type, unit_team, side, slot):
            Unit.__init__(self, game, x, y, unit_class, unit_type, unit_team, side, slot, walk_frames = 10, attack_frames = 47, damage_frame = 40,
                           attacking_range=150, health = 50, attack = 20,
                           defense = 1, walking_acc=1, walk_width= 96, attack_width= 128,height=128)
     
class UnitHealthBar(pygame.sprite.Sprite):
    def __init__(self, x,y, filename, game, master, front = True):
        pygame.sprite.Sprite.__init__(self)
        self.filename = filename
        self.game = game
        self.master = master
        self.front = front
        self.max = self.master.health

        self.image = pygame.image.load(self.filename)
        self.image = pygame.transform.scale(self.image, (20,3))
        self.rect = self.image.get_rect()
        self.rect.left = x - 10
        self.rect.centery = y

    def update(self):
        if self.front:
            self.image = pygame.transform.scale(self.image, (int(self.master.health/self.max*20), 3))
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.centery = self.master.rect.centerx-10, self.master.rect.top
        else:
            self.rect.left, self.rect.centery = self.master.rect.centerx-10, self.master.rect.top

    
          
            