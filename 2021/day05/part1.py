
points = {}

with open("input", "r") as f:

	for line in f:
		pointA = (int(line.strip().split(" -> ")[0].split(",")[0]), int(line.strip().split(" -> ")[0].split(",")[1]))
		pointB = (int(line.strip().split(" -> ")[1].split(",")[0]), int(line.strip().split(" -> ")[1].split(",")[1]))
	

		if (pointA[0] != pointB[0]) and (pointA[1] != pointB[1]):
			continue

		x_bounds = sorted([pointA[0], pointB[0]])
		y_bounds = sorted([pointA[1], pointB[1]])
		
		
		for x in range(x_bounds[0], x_bounds[1]+1):
			for y in range(y_bounds[0], y_bounds[1]+1):
				if (x, y) in points.keys():
					points[(x, y)] += 1
				else:
					points[(x, y)] = 1
					
					
count = [1 for p in points.values() if p>=2]
print("Number of points: {}".format(len(count)))
