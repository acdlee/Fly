import pygame

#set the font for our text
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 30)	

#set some colors that we'll use for input boxes
ACTIVE = pygame.Color(253,255,50)
INACTIVE = pygame.Color(0,0,0)
DEFAULT = pygame.Color(105,105,105)

class InputBox(object):	
	"""Class representation of an input box."""
	def __init__(self, x, y, w, h, default):
		self.active = False
		self.rect = pygame.Rect(x, y, w, h)
		self.color =INACTIVE
		self.default = default
		self.text = default
		self.txt_surface = font.render(self.text, True, DEFAULT)

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
		self.txt_surface = font.render(self.text, True, DEFAULT)

	def handle_event(self, event, screen):
		#if they finished typing
		if event.key == pygame.K_RETURN:
			#store the text
			print(self.text)
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
		rect = self.rect
		pygame.draw.rect(screen, (0, 255, 0), rect, 0)		













