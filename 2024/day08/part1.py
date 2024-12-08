#! /usr/bin/python3

from itertools import combinations

def create_antinodes(p1, p2):
    delta_x = p1[0] - p2[0]
    delta_y = p1[1] - p2[1]

    anti1 = (p1[0] + delta_x, p1[1] + delta_y)
    anti2 = (p2[0] - delta_x, p2[1] - delta_y)
    return (anti1, anti2)

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