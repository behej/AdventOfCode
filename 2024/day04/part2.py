#! /usr/bin/python3

array = []

def check_x_mas(x, y):
    if (array[y-1][x-1] == "M" and array[y+1][x+1] == "S") or (array[y-1][x-1] == "S" and array[y+1][x+1] == "M"):
        if (array[y+1][x-1] == "M" and array[y-1][x+1] == "S") or (array[y+1][x-1] == "S" and array[y-1][x+1] == "M"):
            return 1
        
    return 0


with open("input", "r") as f:
    for l in f:
        array.append(l.strip())


counter = 0
for y in range(1, len(array)-1):
    for x in range(1, len(array[0])-1):
        if array[y][x] == "A":
            counter += check_x_mas(x, y)
          


print(counter)