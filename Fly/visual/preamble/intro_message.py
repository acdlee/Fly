import pygame

#init the font from pygame
pygame.font.init()

#this function creates and formats the list
#of instructions for our flight visualization. 
def generate_intro(screen):
	#text settings
	intro_txt = 'Welcome to Fly!\n'
	intro_txt += 'Instructions:\n'
	intro_txt += '~Look at the map for a list of available airports,\n'
	intro_txt += "~Click on either the 'TO:' or 'FROM:' box,\n"
	intro_txt += "~Type where you're headed in the 'TO:' box,\n"
	intro_txt += "~~~Then hit enter,\n"
	intro_txt += "~Type where you're coming from in the 'FROM:' box,\n"
	intro_txt += "~~~Then hit enter,\n"
	intro_txt += "~Finally, hit 'F' on your keyboard to fly!"
	intro_txt += "\n\n\nHit 'S' on your keyboard now to start flying."
	intro_txt += "\n\n\nSafe travels! :)"

	#Call our helper function
	render_multi_line(intro_txt, 0, 100, 30, screen)


#This helper function makes formatting of multi-line
#text in pygame a bit easier. 
def render_multi_line(text, x, y, fsize, screen):
	pygame.init()
	font = pygame.font.Font('freesansbold.ttf', 30)	

	lines = text.splitlines()
	for i, l in enumerate(lines):
		screen.blit(font.render(l, 0, (0, 180, 30)), (x, y + fsize*i))