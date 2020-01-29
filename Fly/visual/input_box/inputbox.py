import pygame

#set the font for our text
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 30)	

#set some colors that we'll use for input boxes
ACTIVE = pygame.Color(253,255,50)
INACTIVE = pygame.Color(0,0,0)
DEFAULT_COLOR = pygame.Color(105,105,105)

class InputBox(object):	
	"""Class representation of an input box."""
	def __init__(self, x, y, w, h, default):
		self.active = False
		self.rect = pygame.Rect(x, y, w, h)
		self.color =INACTIVE
		self.default = default
		self.text = default
		self.txt_surface = font.render(self.text, True, DEFAULT_COLOR)

	#draw the text and the rect to the screen
	def draw(self, screen):
		# Blit the text.
		screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
		# Blit the rect.
		pygame.draw.rect(screen, self.color, self.rect, 2)

	#Changes the color of the input box if it's active
	def check_active(self):
		if self.active:
			self.color = ACTIVE
		else:
			self.color = INACTIVE

	#This method udpates the text of the input box
	def update_text(self):
		self.txt_surface = font.render(self.text, True, DEFAULT_COLOR)

	#This function processes keyboard input into our
	#input boxes. 
	def handle_event(self, event, screen, plane):
		#if they just selected the box and are about to type,
		#remove the default text.
		if self.text == self.default:
			self.text = ''
			self.update_text()
			self.reset_box(screen)

		#if they finished typing, attempt to store the text
		if event.key == pygame.K_RETURN:
			#check if input text is an airport in our system
			if plane.system.search_airports(self.text) != None:
				#if it's the TO: input box, store in plane.going_to
				if self.default == 'TO:':
					plane.going_to = self.text	
				#else store in plane.going_from
				else:
					plane.coming_from = self.text

			#and reset the input box
			self.text = self.default
			self.reset_box(screen)
		#delete the previous char given backspace input
		elif event.key == pygame.K_BACKSPACE:
			self.text = self.text[:-1]
			self.reset_box(screen)
			#check if there's no text
			if not len(self.text):
				#set to default if empty
				self.text = self.default
		else:
			self.text += event.unicode

		#Re-render the text
		self.update_text()

	#This function recolors the input box; ie, 
	#gets rid of the old text.
	def reset_box(self, screen):
		pygame.draw.rect(screen, (0, 255, 0), self.rect, 0)		













