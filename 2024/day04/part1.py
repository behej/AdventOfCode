#! /usr/bin/python3

xmas = "MAS"
array = []

def check_right(x, y):
    for (i,l) in enumerate(xmas, start=1):
        if array[y][x+i] != l:
            return 0
    return 1

def check_left(x, y):
    for (i,l) in enumerate(xmas, start=1):
        if array[y][x-i] != l:
            return 0
    return 1

def check_down(x, y):
    for (i,l) in enumerate(xmas, start=1):
        if array[y+i][x] != l:
            return 0
    return 1

def check_up(x, y):
    for (i,l) in enumerate(xmas, start=1):
        if array[y-i][x] != l:
            return  0
    return 1

def check_right_down(x, y):
    for (i,l) in enumerate(xmas, start=1):
        if array[y+i][x+i] != l:
            return 0
    return 1

def check_right_up(x, y):
    for (i,l) in enumerate(xmas, start=1):
        if array[y-i][x+i] != l:
            return 0
    return 1

def check_left_down(x, y):
    for (i,l) in enumerate(xmas, start=1):
        if array[y+i][x-i] != l:
            return 0
    return 1
        
def check_left_up(x, y):
    for (i,l) in enumerate(xmas, start=1):
        if array[y-i][x-i] != l:
            return 0
    return 1
        

with open("input", "r") as f:
    for l in f:
        array.append(l.strip())


counter = 0
for y in range(len(array)):
    for x in range(len(array[0])):
        if array[y][x] == "X":
            if x <= (len(array[0]) - 4):
                counter += check_right(x, y)
            if x >= 3:
                counter += check_left(x, y)
            if y <= (len(array) - 4):
                counter += check_down(x, y)
            if y >= 3:
                counter += check_up(x, y)
            if (x <= (len(array[0]) - 4)) and (y <= (len(array) - 4)):
                counter += check_right_down(x, y)
            if (x <= (len(array[0]) - 4)) and (y >= 3):
                counter += check_right_up(x, y)
            if (x >= 3) and (y <= (len(array) - 4)):
                counter += check_left_down(x, y)
            if (x >= 3) and (y >= 3):
                counter += check_left_up(x, y)



print(counter)