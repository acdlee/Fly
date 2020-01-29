import pygame, sys
sys.path.append('../airport_system/')
import generate_airports

#This function will draw connecting lines based
#off airports that can travel to one another. 
def draw_connects(screen, system):
	#have a list of airports we've already drawn lines for
	#to avoid duplicate lines. 
	lines = []

	#for each airport in our list of airports
	for airport in system.airports:
		#grab the start location of the line
		location_a = airport.location

		#for each connect in the current airport's list of connected
		#airports, draw a line.
		for connect in airport.connects:
			#if we havent drawn the line yet...
			bool_condition_a = (airport.name, connect) not in lines
			bool_condition_b = (connect, airport.name) not in lines
			if bool_condition_a and bool_condition_b:

				#search_aiports(), defined in airports.py, takes an
				#airport name and returns the index of the corresponding
				#airport in the system of airports. 
				index = system.search_airports(connect)

				#if we didn't find the airport, report an error
				if index == None:
					err_msg = "Airport '" + airport.name + "' has '" + connect
					err_msg += "' in its list of connects, but no such"
					err_msg += " airport exists in our list of airports."
					print(err_msg)
					sys.exit()
				else:
					#else find the index of the connected airport
					location_b = system.airports[index].location


					#then draw the connecting line and add the line to 
					#the list of lines already drawn.
					pygame.draw.line(screen, (222,184,135), location_a, location_b, 2)
					lines.append((airport.name, connect))

#this function draws the airports
#(the names of the airports) to the screen.
def draw_airports(screen, system):
	#set the font of an airport name to be written on the screen
	font = pygame.font.Font('freesansbold.ttf', 12)

	#set up some colors for the text object
	white = (255, 255, 255)
	black = (0,0,0)

	#draw each airport to the screen
	for airport in system.airports:
		#set the text
		text = font.render(airport.name, True, black, white)

		#create a text object
		textRect = text.get_rect()
		textRect.center = airport.location

		#draw the text
		screen.blit(text, textRect)

#This function sets up the rest of the functions
#in this file by generating the system of airpots.
#Then this function calls on those aforementioned functions
#with the appropriate parameters. 
#Note: the function calls the function generate() from
#the file generate_airports; this file is home to
#the Airport objects of our system of airports.
def setup(screen):
	#create the airport system
	system = generate_airports.generate()

	#draw the lines that connect the airports
	draw_connects(screen, system)

	#set background imagine
	#Note: setting the background occurs here, simply as
	#a design choice; I'd rather have the layering be: 
	#Names on top of background on top of connects. 
	background = pygame.image.load('images/map.png')
	screen.blit(background, (0,0))

	#then draw the airports (their names) to the 
	#screen.
	draw_airports(screen, system)

	#return the airport system at the end
	return system



#draw to the screen while we fly; don't re-generate the airports
def flying_screen(screen, system):
	#draw the lines that connect the airports
	draw_connects(screen, system)

	#set background image and screen color - RGB
	background_color = (0, 255, 0)
	screen.fill(background_color)
	background = pygame.image.load('images/map.png')
	screen.blit(background, (0,0))

	#then draw the airports (their names) to the 
	#screen.
	draw_airports(screen, system)
