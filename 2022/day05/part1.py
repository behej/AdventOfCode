#! /bin/python3

import re

COLS = 9
stacks = []

for i in range(COLS):
    stacks.append([])

with  open("input", "r") as f:
    for l in f:
        if l.strip() == "":
            break

        for i in range(COLS):
            crate = l[i*4+1]
            if crate != " " and not crate.isdigit():
                stacks[i].append(crate)

    for s in stacks:
        s.reverse()

    for l in f:
        res = re.match("^move (\d+) from (\d+) to (\d+)$", l.strip())
        qty = int(res.group(1))
        orig = int(res.group(2)) - 1
        dest = int(res.group(3)) - 1

        for i in range(qty):
            stacks[dest].append(stacks[orig].pop())


word = "".join([s[-1] for s in stacks])
print(word)
