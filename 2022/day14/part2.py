#! /usr/bin/python3

max_y = 0

points = {}
start = (500,0)


with open('input', 'r') as f:
	for l in f:
		l = l.strip().split(' -> ')

		for i in range(len(l) - 1):
			[x1, y1] = l[i].split(',')
			[x2, y2] = l[i+1].split(',')
			x1 = int(x1)
			y1 = int(y1)
			x2 = int(x2)
			y2 = int(y2)

			max_y = max(max_y, y1)

			[x1, x2] = sorted([x1, x2])
			[y1, y2] = sorted([y1, y2])

			for j in range(x1, x2+1):
				for k in range(y1, y2+1):
					points[(j, k)] = '#'

		[x1, y1] = l[-1].split(',')
		x1 = int(x1)
		y1 = int(y1)
		max_y = max(max_y, y1)

max_y += 2
counter = 0

while start not in points:
	sand = start
	counter += 1
	while True:
		if (sand[1]+1) >= max_y:
			points[sand] = 'o'
			break
		elif (sand[0], sand[1]+1) not in points.keys():
			sand = (sand[0], sand[1]+1)
		elif (sand[0]-1, sand[1]+1) not in points.keys():
			sand = (sand[0]-1, sand[1]+1)
		elif (sand[0]+1, sand[1]+1) not in points.keys():
			sand = (sand[0]+1, sand[1]+1)
		else:
			points[sand] = 'o'
			break


print(counter)
