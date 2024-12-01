#! /usr/bin/python3

import re


valid = 0


with open("input", "r") as f:
	for l in f:
		res = re.match("^(\d+)-(\d+) ([a-z]): ([a-z]+)$", l.strip())
		min = int(res.group(1))
		max = int(res.group(2))
		car = res.group(3)
		password = res.group(4)

		if min <= password.count(car) <= max:
			valid += 1

print(valid)
