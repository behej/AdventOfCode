#! /usr/bin/python3

l = open("input", "r").readline()

floor = 0
for i, c in enumerate(l):
    floor += 1 if c == '(' else -1
    if floor < 0:
        break
print(i+1)
    
