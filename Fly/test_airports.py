import unittest
from airports import Airport, Airports

class TestAirportMethods(unittest.TestCase):
	"""Testing the methods from airports.py"""

	#create some default airports to work with
	def setUp(self):
		self.LAX = Airport('LAX', (200, 20), ['Eugene'])
		self.Eugene = Airport('Eugene', (100, 30), ['LAX'])	#oregon
		self.SEA = Airport('Seattle-Tacoma', (20, 50), ['Eugene'])	#washington

	#verify that airports have the correct informatioin 
	#concerning name, location, and connected airports.
	def test_creating_airport(self):
		#name, location, connects
		self.assertEqual(self.LAX.name, 'LAX')
		self.assertEqual(self.Eugene.location, (100, 30))
		self.assertEqual(self.SEA.connects, ['Eugene'])



#run the tests
if __name__ == '__main__':
    unittest.main()		