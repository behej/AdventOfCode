#! /usr/bin/python3

import math

initial_map = []
direction = 0  # 0:up, 1:right, 2:down, 3:left

def turn(dir):
    return (dir + 1) % 4

def in_map(pos):
    if (0 <= pos[0] < len(map)) and (0 <= pos[1] < len(map[0])):
        return True
    else:
        return False

def can_move(pos, dir):
    # print(pos, dir)
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
        
def can_place_obstacle(pos, dir):
    if not in_map(move(pos, dir)):
        return False
    
    return initial_map[move(pos, dir)[0]][move(pos, dir)[1]] == "."


def place_obstacle(pos, dir):
    return (move(pos, dir))



with open("input", "r") as f:
    for y,l in enumerate(f):
        initial_map.append(l.strip())
        if "^" in l:
            initial_guard = (y, l.index("^"))


initial_path = {}

guard = initial_guard
map = [list(l) for l in initial_map]

while in_map(guard):
    if can_move(guard, direction):
        if guard in initial_path:
            initial_path[guard].append(direction)
        else:
            initial_path[guard] = [direction]
        guard = move(guard, direction)
    else:
        direction = turn(direction)


del(initial_path[initial_guard])



obstacles = []

for i,p in enumerate(initial_path.keys()):
    progress = int((i+1) / len(initial_path) * 50)    
    print("#" * progress + "." * (50-progress), end="\r")
    
    guard = initial_guard
    direction = 0
    path = {}
    map = [list(l) for l in initial_map]
    map[p[0]][p[1]] = "#"

    while in_map(guard):
        if can_move(guard, direction):
            if guard in path:
                path[guard].append(direction)
            else:
                path[guard] = [direction]
            guard = move(guard, direction)
        else:
            direction = turn(direction)

        

        if guard in path and direction in path[guard]:
            obstacles.append(p)
            break

print()
print(len(obstacles))