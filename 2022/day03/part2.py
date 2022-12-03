#! /bin/python3

def calc_priority(item):
    if item >= 'a' and item <= 'z':
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


priorities = 0
with open("input", "r") as f:
    for l in f:
        g1 = l.strip()
        g2 = f.readline().strip()
        g3 = f.readline().strip()

        common_item = list(set(g1).intersection(g2).intersection(g3))[0]
        priorities += calc_priority(common_item)

print(priorities)
