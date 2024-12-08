#! /usr/bin/python3

from itertools import combinations

def create_antinodes(p1, p2):
    a = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = p1[1] - a * p1[0]

    l = []

    if abs(a) >= 0.5:
        for x in range(dimensions[0]):
            y = a*x + b
            if abs(y - round(y)) < 1e-6:
                l.append((x, int(round(y))))
    else:
        for y in range(dimensions[1]):
            x = (y-b) / a
            if abs(x - round(x)) < 1e-6:
                l.append((int(round(x)),y))

    return l


def in_map(c):
    if 0 <= c[0] < dimensions[0]:
        if 0<= c[1] < dimensions[1]:
            return True
    return False



antennas = {}
map = []

with open("input", "r") as f:
    for l in f:
        map.append(l.strip())

dimensions = (len(map[0]), len(map))

for y,l in enumerate(map):
    max_x = len(l)
    for x,c in enumerate(l.strip()):
        if c != ".":
            if c in antennas.keys():
                antennas[c].append((x,y))
            else:
                antennas[c] = [(x,y)]

antinodes = set()

for key in antennas.keys():
    for pair in list(combinations(antennas[key], 2)):
        coords = create_antinodes(pair[0], pair[1])
        for c in coords:
            if in_map(c):
                antinodes.add(c)

print(len(antinodes))