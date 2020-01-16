from math import sqrt

class Airport(object):
	"""Representation of a city."""
	def __init__(self, name, location, connects):
		self.name = name	#name of the airport
		self.location = location	#(x, y) location on map
		self.connects = connects	#string list of connected airports


class Airports(object):
	"""Represenation of Cities"""
	def __init__(self):
		self.airports = []	#list of airport names
		self.distances = {} #hashmap of distances between airports

	#Function that adds a new_airport to the list of airports. 
	def add_airport(self, name, location, connections):
		if name not in self.airports:
			new_airport = Airport(name, location, connections)
			self.airports.append(new_airport)
	
	#This function finds the distances between 
	#airports a and b.
	#Note: We're only interested in distance here; we'll have
	#a seperate function when actually traveling to/from airports.
	def get_distance(self, airport_a, airport_b):	
		#Check if we already know the distance
		if (airport_a, airport_b) in self.distance:
			return self.distance[(airport_a, airport_b)]

		if (airport_b, airport_a) in self.distance:
			return self.distance[(airport_b, airport_a)]

		#Find the indicies of the airports;
		#return -1 (an invalid distance) if either
		#airports do not exist in the list of airports.
		try:
			index_a = self.airports.index(airport_a)
			index_b = self.airports.index(airport_b)
		except ValueError as e:
			return -1	#Error case
		else:
			#(x, y) coords of both airports
			(x_a, y_a) = self.airports[index_a].location
			(x_b, y_b) = self.airports[index_b].location

			#Apply distance formula: sqrt[ (x2 - x1)^2 + (y2 - y1)^2]
			distance = ((x_a - x_b)**2) + ((y_a - y_b)**2)
			distance = sqrt(distance)

			#Add the new distance to the dictionary of distances
			self.distances[(airport_a, airport_b)] = distance
			
			return distance
















