import pygame, sys
import collision_boxes as cb
#Event checker:
#Exit (through window) or 'q' ==> exit (and quit) game
def check_event(screen, input_box1, input_box2):
	for event in pygame.event.get():
		#if the user quits
		if event.type == pygame.QUIT:
			sys.exit()
		#if the user clicks with the mouse
		elif event.type == pygame.MOUSEBUTTONDOWN:
			cb.collision_check(input_box1, input_box2, event, screen)
		#if the user is typing
		elif event.type == pygame.KEYDOWN:
			#check if they're typing in an input box
			if input_box1.active:
				input_box1.handle_event(event, screen)
			elif input_box2.active:
				input_box2.handle_event(event, screen)