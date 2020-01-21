import pygame
import settings
import event_checker
import plane
import inputbox

#init pygame
pygame.init()

#create our screen/game window; inclues drawing cities
screen = settings.set_screen()

#game clock
clock = pygame.time.Clock()

#create our input boxes
input_box1 = inputbox.InputBox(300, 500, 180, 40, 'TO:')
input_box2 = inputbox.InputBox(500, 500, 180, 40, 'FROM:')

#create our plane
plane = plane.Plane(screen)

while True: 
	#check events
	event_checker.check_event(screen, input_box1, input_box2)

	#draw some rectangles
	input_box1.draw(screen)
	input_box2.draw(screen)

	#Draw the plane
	plane.update()

	#Draw to screen and tick
	pygame.display.flip()
	clock.tick(20)
