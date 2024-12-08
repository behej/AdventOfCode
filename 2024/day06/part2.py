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
    
    return map[move(pos, dir)[0]][move(pos, dir)[1]] == "."


def place_obstacle(pos, dir):
    return (move(pos, dir))



with open("input", "r") as f:
    for y,l in enumerate(f):
        map.append(l.strip())
        if "^" in l:
            initial_guard = (y, l.index("^"))


counter = 0
obstacles = set()
stop = False

while not stop:
    guard = initial_guard
    direction = 0
    visited = {}
    loop_detected = False
    iteration = 0
    

    while in_map(guard) and not loop_detected:
        if iteration == counter:
            if can_place_obstacle(guard, direction):
                obstacle = place_obstacle(guard, direction)
                # print("place obstaxle", obstacle)
                direction = turn(direction)


        if can_move(guard, direction):
            if guard in visited.keys():
                visited[guard].append(direction)
            else:
                visited[guard] = [direction]
            guard = move(guard, direction)
        else:
            direction = turn(direction)

        if guard in visited:
            if direction in visited[guard]:
                # print("loop_detected")
                loop_detected = True
                obstacles.add(obstacle)

        iteration += 1

    if iteration <= counter:
        stop = True
    counter += 1


print(obstacles)
print(len(obstacles))