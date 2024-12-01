#! /usr/bin/python3

with open("input", "r") as f:
	pass

with open("input", "r") as f:
	list1 = []
	list2 = []
		
	for line in f:
		list1.append(int(line.split()[0]))
		list2.append(int(line.split()[1]))


similarity = 0

for i in list1:
	similarity += i * list2.count(i)



print(similarity)
