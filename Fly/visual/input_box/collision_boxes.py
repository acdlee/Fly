#this function checks if either input box has been 
#selected for input. 
#This function also calls each box'ss check_active()
#method, which changes the color of the input box.
#Note: only one box can be active at a time.  
def collision_check(input_box1, input_box2, event, screen):
	#check if user clicks on the input box
	if input_box1.rect.collidepoint(event.pos):
		input_box1.active = True
		input_box2.active = False
		#remove the default text for the active box
		input_box1.reset_box(screen)
	elif input_box2.rect.collidepoint(event.pos):
		input_box2.active = True
		input_box1.active = False
		#remove the default text for the active box
		input_box2.reset_box(screen)
	else:
		input_box1.active = False
		input_box2.active = False
	#Call this function to set the colo based on 
	#the input box being active. 
	input_box1.check_active()
	input_box2.check_active()
