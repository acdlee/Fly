import pygame

#Set up the screen settings for the introduction while loop
def generate_screen():
	#dimensions of window
	(width, height) = (800, 600)
	screen = pygame.display.set_mode((width, height))

	#window title
	pygame.display.set_caption('Fly - Preamble')

	#screen color - RGB
	background_color = (11, 11, 41)
	screen.fill(background_color)

	#return the created screen
	return screen