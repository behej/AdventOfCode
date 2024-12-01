#! /usr/bin/python3

import re


valid = 0


with open("input", "r") as f:
	for l in f:
		res = re.match("^(\d+)-(\d+) ([a-z]): ([a-z]+)$", l.strip())
		pos1 = int(res.group(1)) - 1
		pos2 = int(res.group(2)) - 1
		car = res.group(3)
		password = res.group(4)

		if (password[pos1] == car and password[pos2] != car) or (password[pos1] != car and password[pos2] == car):
			valid += 1

print(valid)
