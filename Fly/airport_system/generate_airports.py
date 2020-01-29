from airports import Airport, Airports

#this function generates Airport objects that will be 
#drawn to our pygame window. 
def generate():
	#individual airports
	LAX = Airport('LAX', (120, 190), ['Eugene', 'Las Vegas'])	#Cali
	Eugene = Airport('Eugene', (140, 80), ['LAX', "Las Vegas"])	#oregon
	SEA = Airport('Tacoma', (140, 30), ['Eugene'])	#washington
	Nev = Airport('Las Vegas', (160, 160), ['LAX', 'Eugene']) #nevada

	#list of airports
	lst = [LAX, Eugene, SEA, Nev]

	#Create the system of airports; then add the lst of Airports
	system = Airports()
	system.add_airports(lst)

	#return the system of Airport objects
	return system
