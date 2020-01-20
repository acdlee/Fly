import pygame, sys
sys.path.append('../airport_system/')
import generate_airports
import illustrate


#this function does some initial setup for the screen.
#this includes background, dimmensions, and drawing
#the airports.
def set_screen():
	#dimensions of window
	(width, height) = (800, 600)
	screen = pygame.display.set_mode((width, height))

	#window title
	pygame.display.set_caption('Fly')

	#screen color - RGB
	background_color = (0, 255, 0)
	screen.fill(background_color)

	#call a helper function to help draw the cities
	illustrate.setup(screen)

	return screen