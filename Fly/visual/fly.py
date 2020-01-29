import pygame, sys
import settings, event_checker
sys.path.append('./visual_aid/')
sys.path.append('./input_box/')
sys.path.append('./preamble')
import inputbox, plane, intro
sys.path.append('./visual_aid/')
import illustrate

#to give the user some instructions, call the intro
intro.preamble()

#init pygame
pygame.init()

#create our screen/game window; inclues drawing cities
screen, system = settings.set_screen()

#game clock
clock = pygame.time.Clock()

#create our input boxes
input_box1 = inputbox.InputBox(300, 500, 180, 40, 'TO:')
input_box2 = inputbox.InputBox(500, 500, 180, 40, 'FROM:')

#create our plane
plane = plane.Plane(screen, system)

#Flight visualization while loop
while True: 
	#check events
	event_checker.check_event(screen, input_box1, input_box2, plane)

	#draw some rectangles
	input_box1.draw(screen)
	input_box2.draw(screen)

	#if the plane is flying, we have to erase prior blits
	if plane.flying:
		illustrate.flying_screen(screen, system)

	#Draw the plane
	plane.update()

	#Draw to screen and tick
	pygame.display.flip()
	clock.tick(10)
