import pygame
from math import floor, sqrt

class Plane(pygame.sprite.Sprite):
	"""Draw a plane"""
	def __init__(self, screen, system):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		self.image = pygame.image.load('images/planejane.bmp')
		self.rect = self.image.get_rect()
		self.rect.x = 80
		self.rect.y = screen.get_height() - 100
		self.going_to = ''
		self.coming_from = ''
		self.slope = 0
		self.flying = False
		self.system = system
		self.destination = 0

	#This method draws the plane to the screen
	def update(self):

		#if flying, adjust based on slope
		#check if we've reached our destination; 
		#when we've reached the destination, flip
		#flying to False again and reset the to and from
		if self.flying:
			self.rect.y += self.slope
			self.rect.x += 1

			#check if we've reached our destination
			self.are_we_there_yet()

		#Draw the plane
		self.screen.blit(self.image, self.rect)

	def set_slope(self):
		#find the airport index
		index_a = self.system.search_airports(self.going_to)
		index_b = self.system.search_airports(self.coming_from)

		#find their actual locations
		x_a, y_a = self.system.airports[index_a].location
		x_b, y_b = self.system.airports[index_b].location

		#calc the slope
		y2minusy1 = y_b - y_a
		x2minusx1 = x_b - x_a

		#set the slope
		self.slope = y2minusy1//x2minusx1

		#set the destination coord
		self.destination = (x_a, y_a)

		#move the plane to the start location
		self.rect.x = x_b
		self.rect.y = y_b

	def are_we_there_yet(self):
		x_a, y_a = self.destination
		x_b, y_b = self.rect.x, self.rect.y
		#Apply distance formula: sqrt[ (x2 - x1)^2 + (y2 - y1)^2]
		distance = ((x_a - x_b)**2) + ((y_a - y_b)**2)
		distance = floor(sqrt(distance))		

		#if we're close enough, reset everything
		if distance < 20:
			self.flying = False
			self.going_to = ''
			self.coming_from = ''
			self.rect.x = 80
			self.rect.y = self.screen.get_height() - 100

