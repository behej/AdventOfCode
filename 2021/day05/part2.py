


points = {}

with open("input", "r") as f:

	for line in f:
		pointA = (int(line.strip().split(" -> ")[0].split(",")[0]), int(line.strip().split(" -> ")[0].split(",")[1]))
		pointB = (int(line.strip().split(" -> ")[1].split(",")[0]), int(line.strip().split(" -> ")[1].split(",")[1]))
	
		x_bounds = sorted([pointA[0], pointB[0]])
		y_bounds = sorted([pointA[1], pointB[1]])

		x_step = -1 if (pointA[0] > pointB[0]) else 1
		y_step = -1 if (pointA[1] > pointB[1]) else 1

			
		if (pointA[0] == pointB[0]) or (pointA[1] == pointB[1]):
			for x in range(pointA[0], pointB[0]+x_step, x_step):
				for y in range(pointA[1], pointB[1]+y_step, y_step):
					if (x, y) in points.keys():
						points[(x, y)] += 1
					else:
						points[(x, y)] = 1

		else:
			for (x,y) in zip(range(pointA[0], pointB[0]+x_step, x_step), range(pointA[1], pointB[1]+y_step, y_step)):
				if (x, y) in points.keys():
					points[(x, y)] += 1
				else:
					points[(x, y)] = 1
					
count = [1 for p in points.values() if p>=2]
print("Number of points: {}".format(len(count)))

