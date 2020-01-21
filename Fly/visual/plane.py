import pygame

class Plane(pygame.sprite.Sprite):
	"""Draw a plane"""
	def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		self.image = pygame.image.load('images/planejane.bmp')
		self.rect = self.image.get_rect()
		self.rect.x = 80
		self.rect.y = screen.get_height() - 100

	def update(self):
		#movement will be handled heree

		#Draw the plane
		self.screen.blit(self.image, self.rect)