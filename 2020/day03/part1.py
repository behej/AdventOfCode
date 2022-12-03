#! /usr/bin/python3

import re


coord = (0, 0)
y = 0
count = 0


with open("input", "r") as f:
	width = len(f.readline().strip())
	for l in f:
		y = (y + 3) % width
		if l[y] == '#':
			count += 1


print(count)
