import pygame, sys
import settings_2, event_checker_2, intro_message

#Guides the user through some basic instructions
#for using the flight visualization. 
def preamble():
	
	#initialize pygame
	pygame.init()

	#generate the screen
	screen = settings_2.generate_screen()

	#generate the intstruction text and place it on the screen
	intro_message.generate_intro(screen)

	#game swtich
	running = True

	#introduction screen while loop
	while running:

		#check events
		running = event_checker_2.check_event()

		#draw to game
		pygame.display.flip()





