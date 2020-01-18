import pygame, sys
sys.path.append('../airport_system/')
import generate_airports

#this function, after being called in set_screen, 
#draws the airports to the screen.
#note the function calls the function generate() from
#the file generate_airports; this file is home to
#the Airport objects of our system of airports.
def draw_airports(screen):
	#set the font of an airport name to be written on the screen
	font = pygame.font.Font('freesansbold.ttf', 12)

	#set up some colors for the text object
	white = (255, 255, 255)
	black = (0,0,0)

	#create the airport system
	system = generate_airports.generate()

	#draw each airport to the screen
	for airport in system.airports:
		#set the text
		text = font.render(airport.name, True, black, white)

		#create a text object
		textRect = text.get_rect()
		textRect.center = airport.location

		#draw the text
		screen.blit(text, textRect)


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
	draw_airports(screen)

	return screen