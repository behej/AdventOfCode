#! /usr/bin/python3

with open("input", "r") as f:
	pass

with open("input", "r") as f:
	list1 = []
	list2 = []
		
	for line in f:
		list1.append(int(line.split()[0]))
		list2.append(int(line.split()[1]))

list1.sort()
list2.sort()

distance = 0

for i in zip(list1, list2):
	distance += abs(i[0] - i[1])


print(distance)
