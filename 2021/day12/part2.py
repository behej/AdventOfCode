

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



def find_path(path, small_cave_visited_twice):
	global routes
	
	if path[-1] == "end":
		routes.append(path)
		return
		
	for c in map[path[-1]].connections:
		# considered cave (if small) is not already in path
		if not map[c].is_small() or c not in path:
			local_path = list(path)
			local_path.append(c)
			find_path(local_path, small_cave_visited_twice)
		# considered case (if small) is already in path but no small cave has been visited twice yet)
		elif map[c].is_small() and c in path and not small_cave_visited_twice and c != "start":
			local_path = list(path)
			local_path.append(c)
			find_path(local_path, small_cave_visited_twice=True)
			


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
find_path(["start"], small_cave_visited_twice=False)
print("There are {} differents routes".format(len(routes)))

