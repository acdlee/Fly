import pygame
import settings
import event_checker

screen = settings.get_screen()



while True: 
	#check events
	event_checker.check_event()

	#Draw a circle
	#pygame.draw.circle(screen, (255, 255, 255), (800, 0), 30)

	#Draw to screen
	pygame.display.flip()