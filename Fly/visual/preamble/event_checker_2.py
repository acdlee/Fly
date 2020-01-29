import sys, pygame

#This function checks the events of the preamble 
#(introduction) while loop
def check_event():
	for event in pygame.event.get():
		#if the user quits
		if event.type == pygame.QUIT:
			sys.exit()
		#check if the user is ready to move on
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				#Flip running to False
				return False
	#if still reading, dont flip running to False
	return True