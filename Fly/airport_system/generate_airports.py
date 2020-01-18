from airports import Airport, Airports

#this function generates Airport objects that will be 
#drawn to our pygame window. 
def generate():
	#individual airports
	LAX = Airport('LAX', (600, 40), ['Eugene'])	#Cali
	Eugene = Airport('Eugene', (300, 80), ['LAX'])	#oregon
	SEA = Airport('Seattle-Tacoma', (100, 100), ['Eugene'])	#washington

	#list of airports
	lst = [LAX, Eugene, SEA]

	#Create the system of airports; then add the lst of Airports
	system = Airports()
	system.add_airports(lst)

	#return the system of Airport objects
	return system
