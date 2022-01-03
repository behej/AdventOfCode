
low_points = []

lines = []


with open("input", "r") as f:
	for l in f:
		lines.append(l.strip())
		


# top left corner
if lines[0][0] < lines[1][0] and lines[0][0] < lines[0][1]:
	low_points.append(lines[0][0])
# top right corner
if lines[0][-1] < lines[1][-1] and lines[0][-1] < lines[0][-2]:
	low_points.append(lines[0][-1])
# bottom left corner
if lines[-1][0] < lines[-2][0] and lines[-1][0] < lines[-1][1]:
	low_points.append(lines[-1][0])
# bottom right corner
if lines[-1][-1] < lines[-1][-2] and lines[-1][-1] < lines[-2][-1]:
	low_points.append(lines[-1][-1])
	
# 1st and last rows (except corners)
for x in range(1, len(lines[0])-1):
	# 1st row
	if (lines[0][x] < lines[0][x-1] ) and (lines[0][x] < lines[0][x+1]) and (lines[0][x] < lines[1][x]):
		low_points.append(lines[0][x])
	# last row
	if (lines[-1][x] < lines[-1][x-1] ) and (lines[-1][x] < lines[-1][x+1]) and (lines[-1][x] < lines[-2][x]):
		low_points.append(lines[-1][x])

# 1st and last columns (except corners)
for y in range(1, len(lines)-1):
	# 1st column
	if (lines[y][0] < lines[y-1][0] ) and (lines[y][0] < lines[y+1][0]) and (lines[y][0] < lines[y][1]):
		low_points.append(lines[y][0])
	# last column
	if (lines[y][-1] < lines[y-1][-1] ) and (lines[y][-1] < lines[y+1][-1]) and (lines[y][-1] < lines[y][-2]):
		low_points.append(lines[y][-1])
		
# All other points		
for y in range(1, len(lines)-1):
	for x in range(1, len(lines[y])-1):
		if (lines[y][x] < lines[y][x-1]) and (lines[y][x] < lines[y][x+1]) and (lines[y][x] < lines[y-1][x]) and (lines[y][x] < lines[y+1][x]):
			low_points.append(lines[y][x])


low_points = [int(p) for p in low_points]
risk_levels = sum(low_points) + len(low_points)


print("Sum of risk levels: {}".format(risk_levels))