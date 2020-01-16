import pygame

def get_screen():
	#dimensions of window
	(width, height) = (800, 600)
	screen = pygame.display.set_mode((width, height))

	#window title
	pygame.display.set_caption('Fly ')

	#screen color - RGB
	background_color = (0, 255, 0)
	screen.fill(background_color)

	return screen