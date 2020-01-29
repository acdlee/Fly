from math import sqrt, floor

class Airport(object):
	"""Representation of a city."""
	def __init__(self, name, location, connects):
		self.name = name	#name of the airport
		self.location = location	#(x, y) location on map
		self.connects = connects	#string list of connected airports

	#toString method for an Airport object.
	def __str__(self):
		s = "Airport " + self.name + " is located at"
		s += " " + str(self.location) + " and is connected to"
		s+= " the following ariports: "
		for connect in self.connects:
			s += "\n~" + connect + ","

		#remove the extra comma
		return s[:-1]


class Airports(object):
	"""Represenation of Cities"""
	def __init__(self):
		self.airports = []	#list of airport objects
		self.distances = {} #hashmap of distances between airports

	#Function that adds a new_airport to the list of airports. 
	def add_airport(self, new_airport):
		if new_airport not in self.airports:
			self.airports.append(new_airport)

	#This method will call on add_aiport to add the 
	#parameter list of Airport objects.
	def add_airports(self, airports):
		for airport in airports:
			self.add_airport(airport)
	
	#This method, given an Airport name, searches for
	#the corresponding Airport object; 
	#returns None if not found. 
	def search_airports(self, name):
		name = name.lower()
		for i in range(len(self.airports)):
			if self.airports[i].name.lower() == name:
				return i
		return None

	#This function finds the distances between 
	#the Airport objects airport_a and airport_b.
	#Note: We're only interested in distance here; we'll have
	#a seperate function when actually traveling to/from airports.
	def get_distance(self, airport_a, airport_b):	
		#Check if we already know the distance
		if (airport_a, airport_b) in self.distances:
			return self.distances[(airport_a, airport_b)]

		if (airport_b, airport_a) in self.distances:
			return self.distances[(airport_b, airport_a)]

		#Find the indicies of the airports;
		#return -1 (an invalid distance) if either
		#airports do not exist in the list of airports.
		index_a = self.search_airports(airport_a)
		index_b = self.search_airports(airport_b)
		if index_a == None or index_b == None:
			return -1 #error case
		else:
			#(x, y) coords of both airports
			(x_a, y_a) = self.airports[index_a].location
			(x_b, y_b) = self.airports[index_b].location

			#Apply distance formula: sqrt[ (x2 - x1)^2 + (y2 - y1)^2]
			distance = ((x_a - x_b)**2) + ((y_a - y_b)**2)
			distance = floor(sqrt(distance))

			#Add the new distance to the dictionary of distances
			self.distances[(airport_a, airport_b)] = distance
			
			return distance



