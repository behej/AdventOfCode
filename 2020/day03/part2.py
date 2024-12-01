#! /usr/bin/python3

import math

counts = []
trials = [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]

for t in trials:
	with open("input", "r") as f:
		y = 0
		count = 0
		width = len(f.readline().strip())
		for l in f:
			for i in range(0, t[1] - 1):
				l = f.readline()

			y = (y + t[0]) % width
			if l[y] == '#':
				count += 1

		counts.append(count)

print(math.prod(counts))
