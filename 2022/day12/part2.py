#! /usr/bin/python3

def neighbors(p):
	"""Return all valid neighbors of a given point.

    Valid neighbor means within array bounds and neighbor still present
    in unvisited points and also neighbor must be at most 1 step lower (but
	can be any step higher) - This rule because find path is found reverse."""
	(x, y) = p
	n = []

	for (x_offset, y_offset) in [(-1,0), (0,-1), (1,0), (0,1)]:
		if 0 <= x+x_offset < dimensions[0] and 0 <= y+y_offset < dimensions[1] and \
				(x+x_offset, y+y_offset) in unvisited.keys():
			# Neighbor has to be max 1 step higher but can be any step lower
			if heights[p]-1 <= heights[(x+x_offset, y+y_offset)]:
				n.append((x+x_offset, y+y_offset))

	return n


# Dijkstra algorithm
# ===================
# 1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
# 2. Assign to every node a tentative distance value: set it to zero for our initial node and
#	 to infinity for all other nodes. The tentative distance of a node v is the length of the
#	 shortest path discovered so far between the node v and the starting node.
#	 Since initially no path is known to any other vertex than the source itself (which is a
#	 path of length zero), all other tentative distances are initially set to infinity. Set the initial node as current.
# 3. For the current node, consider all of its unvisited neighbors and calculate their tentative
# 	 distances through the current node. Compare the newly calculated tentative distance to the current
# 	 assigned value and assign the smaller one. Otherwise, the current value will be kept.
# 4. When we are done considering all of the unvisited neighbors of the current node, mark the current
#	 node as visited and remove it from the unvisited set. A visited node will never be checked again.
# 5. If the destination node has been marked visited (when planning a route between two specific nodes) or
#	 if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a
#	 complete traversal; occurs when there is no connection between the initial node and remaining unvisited
#	 nodes), then stop. The algorithm has finished.
# 6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new
#	 current node, and go back to step 3.


unvisited = {}		# list of unvisited points
area = {}			# map of area (each point costs 1, since each move is considered equally)
heights = {}		# map of heights (must be considered to determine accessible neighbors)
# dest = 0			# Destination point not specifically defined, distination is 1st point at altitude 'a'

# Load file
with  open("input", "r") as f:
    lines = f.read().strip().split("\n")
    dimensions = (len(lines[0]),len(lines))

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            area[(x,y)] = 1
            heights[(x,y)] = ord(lines[y][x]) - ord('a')
            if lines[y][x] == 'E':
                heights[(x,y)] = ord('z') - ord('a')
                start = (x,y)   # Start point is set to destination - path will be found reverse
            elif lines[y][x] == 'S':
                heights[(x,y)] = 0
            unvisited[(x,y)] = 999999999


# Init value before algo
unvisited[start] = 0
min_steps = 999999999999

# Start algorithm iteration
while unvisited:
    current = min(unvisited, key=unvisited.get)
    total_steps = unvisited[current]

    # Current point is at lowest height -> path is over
    if heights[current] == 0:
        min_steps = total_steps
        break

    for n in neighbors(current):
        unvisited[n] = total_steps + area[n] if (total_steps + area[n]) < unvisited[n] else unvisited[n]
    del(unvisited[current])

print("Shortest path: {}".format(min_steps))
