

class Cave:
	def __init__(self, name):
		self._name = name
		self.big_cave = name.isupper()
		self.connections = []
		
	def __repr__(self):
		return "Cave '{}' ({} - connected to {})".format(self._name, "big" if self.big_cave else "small", self.connections)
		
	def add_connection(self, other_cave):
		if other_cave not in self.connections:
			self.connections.append(other_cave)
			
	def is_small(self):
		return not self.big_cave



def find_path(path):
	global routes
	
	if path[-1] == "end":
		routes.append(path)
		return
		
	for c in map[path[-1]].connections:
		if not map[c].is_small() or c not in path:
			local_path = list(path)
			local_path.append(c)
			find_path(local_path)
			


map = {}

with  open("input", "r") as f:
	for l in f:
		pointA = l.strip().split("-")[0]
		pointB = l.strip().split("-")[1]
		
		if pointA not in map:
			map[pointA] = Cave(pointA)
		
		if pointB not in map:
			map[pointB] = Cave(pointB)
		
		map[pointA].add_connection(pointB)
		map[pointB].add_connection(pointA)
				
				
		
		
routes = []
find_path(["start"])
print("There are {} differents routes".format(len(routes)))

