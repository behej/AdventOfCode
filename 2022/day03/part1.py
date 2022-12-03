#! /bin/python3

def calc_priority(item):
    if item >= 'a' and item <= 'z':
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


priorities = 0
with open("input", "r") as f:
    for l in f:

        part1 = l[:len(l)//2]
        part2 = l[len(l)//2:]

        common_item = list(set(part1).intersection(part2))[0]
        priorities += calc_priority(common_item)


print(priorities)
