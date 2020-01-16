class Edge():
	"""Edge representation"""
	def __init__(self, v1, v2, distance):
		self.v1 = v1
		self.v2 = v2
		self.distance = distance
		

class Graph(object):
	"""docstring for Graph"""
	def __init__(self):
		self.verticies = []
		self.edges = []
		
	#Add a new edge to our graph; add the verticie args
	#to the graph's list of verticies if necessary. 
	def add_new_edge(self, u, w, distance):
		new_edge = Edge(u, w, distance)
		self.edges.append(new_edge)
		if u not in self.verticies:
			self.verticies.append(u)
		if w not in self.verticies:
			self.verticies.append(w)

	def add_edge(self, e):
		self.edges.append(e)
		if e.v1 not in self.verticies:
			self.verticies.append(e.v1)
		if e.v2 not in self.verticies:
			self.verticies.append(e.v2)

	def has_vertex(self, u):
		return u in self.verticies

	#return the edge distance between two verticies
	def find_edge_distance(self, u, v):
		for e in self.edges:
			if (e.v1 == u and e.v2 == v) or (e.v1 == v and e.v2 == u):
				return e.distance

		return None	#if no edge exists -> return None