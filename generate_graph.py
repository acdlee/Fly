from graph import Graph as G, Edge as E

def create_graph():
	g = G()
	g.add_new_edge('S', 'B', 10)
	g.add_new_edge('S', 'B', 12)
	g.add_new_edge('C', 'B', 15)
	g.add_new_edge('C', 'A', 42)
	g.add_new_edge('A', 'P', 27)
	g.add_new_edge('A', 'F', 44)
	g.add_new_edge('F', 'L', 26)
	g.add_new_edge('F', 'L', 44)
	g.add_new_edge('F', 'G', 26)
	g.add_new_edge('L', 'E', 1)
	g.add_new_edge('B', 'D', 18)
	g.add_new_edge('E', 'D', 9)
	g.add_new_edge('E', 'M', 49)
	g.add_new_edge('E', 'I', 2)
	g.add_new_edge('K', 'I', 32)

	return g
