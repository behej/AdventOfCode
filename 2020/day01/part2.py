#! /usr/bin/python3

list = []


with open("input", "r") as f:
	for l in f:
		list.append(int(l.strip()))


for i in range(0, len(list)):
	for j in range(i, len(list)):
		for k in range(j, len(list)):
			if (list[i] + list[j] + list[k]) == 2020:
				print(list[i] * list[j] * list[k])
				break
