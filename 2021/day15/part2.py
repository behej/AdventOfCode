

def neighbors(p):
	"""Return all valid neighbors of a given point.
	
	Valid neighbor means within array bounds and neighbor still present
	in unvisited points."""

	global dest
	(x, y) = p

	n = []
	
	for (x_offset, y_offset) in [(-1,0), (0,-1), (1,0), (0,1)]:
		if 0 <= x+x_offset <= dest[0] and 0 <= y+y_offset <= dest[1]:
			n.append((x+x_offset, y+y_offset))
	
	return n




open_list = {}
closed_list = {}
tile1 = {}
cave = {}
dest = 0
dimensions = 0
coeff = 5


# Load file
with  open("input", "r") as f:
	lines = f.read().strip().split("\n")
	
	for y in range(len(lines)):
		for x in range(len(lines[y])):
			tile1[(x,y)] = int(lines[y][x])
			
	dimensions = (len(lines[0]) , len(lines))
	

# Extend map by 5 in both dimensions
for p,r in tile1.items():
	for i in range(coeff):
		for j in range(coeff):
			cave[(p[0]+i*dimensions[0], p[1]+j*dimensions[1])] = (r+i+j) % 9 if (r+i+j) != 9 else 9
			
			
dest = (dimensions[0]*coeff - 1, dimensions[1]*coeff - 1)



# A* Search Algorithm
#====================
# 1. Initialize the open list
# 2. Initialize the closed list
#	 put the starting node on the open list (you can leave its f at zero)
# 3. While the open list is not empty
#	a.	find the node with the least f on the open list, call it "q"
# 	b.	pop q off the open list
#   c.	generate q's successors and set their parents to q
#   d.	for each successor
#		i.	 if successor is the goal, stop search
#            successor.g = q.g + distance between successor and q
#            successor.h = distance from goal to successor (Manhattan, Diagonal or Euclidean)
#            successor.f = successor.g + successor.h
#       ii.	 if a node with the same position as successor is in the OPEN list which has a lower f than successor, skip this successor
#       iii. if a node with the same position as successor is in the CLOSED list which has a lower f than successor, skip this successor
#             otherwise, add  the node to the open list
#   e.	push q on the closed list


# Solution = 2872


class Point:
	def __init__(self, g, h=0):
		self.g = g
		self.h = 0
		self.f = self.g + self.h
		
	def __lt__(self, other):
		return (self.f < other.f)
		
	def __eq__(self, other):
		return self.f == other.f




open_list[(0,0)] = Point(0)
min_risk = 999999999999


while open_list:
	current = min(open_list, key=open_list.get)

		
	if current == dest:
		min_risk = open_list[current].g
		break


	for n in neighbors(current):
		g = open_list[current].g + cave[n]
		h = dest[0] - n[0] + dest[1] - n[1]
		f = g + h
		
		if n in open_list.keys() and open_list[n].f < f:
			continue
		if n in closed_list.keys() and closed_list[n].f < f:
			continue
			
		open_list[n] = Point(g, h)
	
	closed_list[current] = open_list[current]
	del(open_list[current])
		
		

print("Minimum risk to reach end: {}".format(min_risk))
