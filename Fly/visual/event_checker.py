import pygame, sys

#Event checker:
#Exit (through window) or 'q' ==> exit (and quit) game
def check_event():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == ord('q'):
				sys.exit()
