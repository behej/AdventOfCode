#! /usr/bin/python3

import math

map = []
direction = 0  # 0:up, 1:right, 2:down, 3:left

def turn(dir):
    return (dir + 1) % 4

def in_map(pos):
    if (0 <= pos[0] < len(map)) and (0 <= pos[1] < len(map[0])):
        return True
    else:
        return False

def can_move(pos, dir):
    if dir == 0:
        if pos[0] == 0:
            return True
        elif map[pos[0] - 1][pos[1]] != "#":
            return True
        
    elif dir == 1:
        if pos[1] == len(map[0]) - 1:
            return True
        elif map[pos[0]][pos[1]+1] != "#":
            return True
        
    elif dir == 2:
        if pos[0] == len(map)-1:
            return True
        elif map[pos[0]+1][pos[1]] != "#":
            return True
        
    elif dir == 3:
        if pos[1] == 0:
            return True
        elif map[pos[0]][pos[1]-1] != "#":
            return True

    else:
        print("Error")

    return False

def move(pos, dir):
    if dir == 0:
        return (pos[0]-1, pos[1])
    elif dir == 1:
        return (pos[0], pos[1]+1)
    elif dir == 2:
        return (pos[0]+1, pos[1])
    elif dir == 3:
        return (pos[0], pos[1]-1)
    else:
        print("Error")
        


with open("input", "r") as f:
    for y,l in enumerate(f):
        map.append(l.strip())
        if "^" in l:
            guard = (y, l.index("^"))

visited = set()

print(guard)
while in_map(guard):
    if can_move(guard, direction):
        visited.add(guard)
        guard = move(guard, direction)
    else:
        direction = turn(direction)


print(len(visited))