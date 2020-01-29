import pygame, sys
sys.path.append('./input_box/')
sys.path.append('./preamble')
import collision_boxes as cb, intro

#Event checker:
#Exit (through window) or 'q' ==> exit (and quit) game
def check_event(screen, input_box1, input_box2, plane):
	for event in pygame.event.get():
		#if the user quits
		if event.type == pygame.QUIT:
			sys.exit()
		#if the user clicks with the mouse
		elif event.type == pygame.MOUSEBUTTONDOWN:
			#the user is not allowed to type in the input box
			#when the plane is flying.
			if not plane.flying:
				cb.collision_check(input_box1, input_box2, event, screen)
		#if the user is typing
		elif event.type == pygame.KEYDOWN:
			#check if they're typing in an input box
			if input_box1.active:
				input_box1.handle_event(event, screen, plane)
			elif input_box2.active:
				input_box2.handle_event(event, screen, plane)
			elif event.key == pygame.K_f:
				#check that plane's to and from are filled
				if plane.going_to != '' and plane.coming_from != '':
					#flip plane.flying to true and everything will
					#update what plane.update() is called
					plane.flying = True

					#and set the slope
					plane.set_slope()


				print('Enjoy your flight!')