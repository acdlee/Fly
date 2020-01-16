import unittest
from airports import Airport, Airports
#import pdb

class TestAirportMethods(unittest.TestCase):
	"""Testing the methods from airports.py"""

	#Create some default airports to work with.
	#Create an airport system (from class Airports) to be used
	#in the later methods. 
	def setUp(self):
		self.LAX = Airport('LAX', (200, 20), ['Eugene'])
		self.Eugene = Airport('Eugene', (100, 30), ['LAX'])	#oregon
		self.SEA = Airport('Seattle-Tacoma', (20, 50), ['Eugene'])	#washington
		self.system = Airports()

	#Test the toString method for an Airport object.
	def test_str(self):
		target = "Airport LAX is located at (200, 20) and is connected"
		target += " to the following ariports: \n~Eugene"
		self.assertEqual((str(self.LAX)), target)

	#verify that airports have the correct informatioin 
	#concerning name, location, and connected airports.
	def test_creating_airport(self):
		#name, location, connects
		self.assertEqual(self.LAX.name, 'LAX')
		self.assertEqual(self.Eugene.location, (100, 30))
		self.assertEqual(self.SEA.connects, ['Eugene'])

	#this method tests adding different airports to our
	#airport system. 
	def test_add_airport(self):
		self.system.add_airport(self.LAX)
		self.assertEqual(self.system.airports[0].name, 'LAX')

	#this method tests the method add_airports which, when 
	#given a list, adds each Airport object in the list to 
	#system.airports.
	def test_add_airports(self):
		lst = [self.Eugene, self.SEA]
		self.system.add_airports(lst)
		self.system.add_airport(self.LAX)
		self.assertEqual(self.system.airports[0].name, 'Eugene')
		self.assertEqual(self.system.airports[1].name, 'Seattle-Tacoma')
		self.assertEqual(self.system.airports[2].name, 'LAX')

	#This method tests the get_distance() method.
	#Note: distance formula: sqrt[ (x2 - x1)^2 + (y2 - y1)^2]
	def test_get_distance(self):
		lst = [self.Eugene, self.SEA, self.LAX]
		self.system.add_airports(lst)
		self.assertEqual(self.system.get_distance('Eugene', 'LAX'), 100)







#run the tests
if __name__ == '__main__':
    unittest.main()		