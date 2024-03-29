import pygame

#button class
class Button():
	def __init__(self, image, x, y, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		global click
		event = False

		#mouse
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			if pygame.mouse.get_pressed()[0] == True and click == False:
				click = True
				event = True

			if pygame.mouse.get_pressed()[0] == False:
				click = False

		surface.blit(self.image, (self.rect.x, self.rect.y))

		return event