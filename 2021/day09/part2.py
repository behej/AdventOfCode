


def explore(coord):
	global lines
	
	
	to_explore = [coord]
	explored = []
	
	while to_explore:
		for i in range(len(to_explore)-1, -1, -1):
			explored.append(to_explore[i])
			(x,y) = to_explore[i]
			del(to_explore[i])
			
			
			# point above
			if (y > 0) and (lines[y-1][x] < "9") and ((x, y-1) not in explored):
				to_explore.append((x, y-1))
			
			# point below
			if (y < (len(lines)-1)) and (lines[y+1][x] < "9") and ((x, y+1) not in explored):
				to_explore.append((x, y+1))
				
			# point left
			if (x > 0) and (lines[y][x-1] < "9") and ((x-1, y) not in explored):
				to_explore.append((x-1, y))

			# point right
			if (x < (len(lines[0])-1)) and (lines[y][x+1] < "9") and ((x+1, y) not in explored):
				to_explore.append((x+1, y))
			
	# remove duplicates
	explored = list(set(explored))
			
	return len(explored)




basins = []
lines = []


with open("input", "r") as f:
	for l in f:
		lines.append(l.strip())
		


# top left corner
if lines[0][0] < lines[1][0] and lines[0][0] < lines[0][1]:
	basins.append(explore((0,0)))
# top right corner
if lines[0][-1] < lines[1][-1] and lines[0][-1] < lines[0][-2]:
	basins.append(explore((len(lines[0])-1,0)))
# bottom left corner
if lines[-1][0] < lines[-2][0] and lines[-1][0] < lines[-1][1]:
	basins.append(explore((0,len(lines)-1)))
# bottom right corner
if lines[-1][-1] < lines[-1][-2] and lines[-1][-1] < lines[-2][-1]:
	basins.append(explore((len(lines[0])-1,len(lines)-1)))


# 1st and last rows (except corners)
for x in range(1, len(lines[0])-1):
	# 1st row
	if (lines[0][x] < lines[0][x-1] ) and (lines[0][x] < lines[0][x+1]) and (lines[0][x] < lines[1][x]):
		basins.append(explore((x,0)))
	# last row
	if (lines[-1][x] < lines[-1][x-1] ) and (lines[-1][x] < lines[-1][x+1]) and (lines[-1][x] < lines[-2][x]):
		basins.append(explore((x,len(lines)-1)))

# 1st and last columns (except corners)
for y in range(1, len(lines)-1):
	# 1st column
	if (lines[y][0] < lines[y-1][0] ) and (lines[y][0] < lines[y+1][0]) and (lines[y][0] < lines[y][1]):
		basins.append(explore((0,y)))
	# last column
	if (lines[y][-1] < lines[y-1][-1] ) and (lines[y][-1] < lines[y+1][-1]) and (lines[y][-1] < lines[y][-2]):
		basins.append(explore((len(lines[0])-1,y)))

		
# All other points		
for y in range(1, len(lines)-1):
	for x in range(1, len(lines[y])-1):
		if (lines[y][x] < lines[y][x-1]) and (lines[y][x] < lines[y][x+1]) and (lines[y][x] < lines[y-1][x]) and (lines[y][x] < lines[y+1][x]):
			basins.append(explore((x,y)))


basins.sort(reverse=True)

multiplication = 1
for i in range(3):
	multiplication *= basins[i]



print("Result: {}".format(multiplication))