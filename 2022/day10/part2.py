#! /usr/bin/python3

def text_px(cycle, reg):
    if (reg-1) <= cycle <= (reg+1):
        tab.append('#')
    else:
        tab.append(' ')

cycle = 0
reg = 1
tab = []

with open('input', 'r') as f:
    for inst in f:
        if inst.strip() == 'noop' or inst.startswith('addx'):
            text_px(cycle%40, reg)
            cycle += 1
        if inst.startswith('addx'):
            text_px(cycle%40, reg)
            cycle += 1

        if inst.startswith('addx'):
            reg += int(inst.split()[1])


for i in range(0, len(tab), 40):
    print(''.join(tab[i:i+40]))
