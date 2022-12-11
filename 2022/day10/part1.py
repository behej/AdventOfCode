#! /usr/bin/python3

cycle = 0
reg = 1
score = 0

with open('input', 'r') as f:
    for inst in f:
        if inst.strip() == 'noop':
            cycle += 1
        if inst.startswith('addx'):
            cycle += 2

        if ((cycle%20 == 0) and (cycle%40 != 0)):
            score += (cycle * reg)
        if (((cycle-1)%20 == 0) and ((cycle-1)%40 != 0) and inst.startswith('addx')):
            score += ((cycle - 1) * reg)

        if inst.startswith('addx'):
            reg += int(inst.split()[1])


print(score)
