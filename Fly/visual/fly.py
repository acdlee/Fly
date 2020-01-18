import pygame
import settings
import event_checker
import plane

#init pygame
pygame.init()

#create our screen/game window; inclues drawing cities
screen = settings.set_screen()

#create our plane
plane = plane.Plane(screen)


while True: 
	#check events
	event_checker.check_event()

	#Draw a circle
	#pygame.draw.circle(screen, (255, 255, 255), (800, 0), 30)

	#Draw the plane
	plane.update()

	#Draw to screen
	pygame.display.flip()