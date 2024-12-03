#! /usr/bin/python3


import re


total = 0
with open("input", "r") as f:
    for txt in f:

        for i in re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", txt):
            total += int(i[4:-1].split(",")[0]) * int(i[4:-1].split(",")[1])

print(total)




