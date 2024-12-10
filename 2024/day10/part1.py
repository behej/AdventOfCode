#! /usr/bin/python3


map = []

def in_map(c):
    return (0 <= c[0] < len(map) and 0 <= c[1] < len(map[0]))


def find_path(c, origin):
    val = map[c[0]][c[1]]

    if val == 0:
        start_points[c].add(origin)
        return
    
    for i,j in [(-1,0), (1,0), (0,1), (0,-1)]:
        new_c = (c[0]+i,c[1]+j)
        if in_map(new_c):
            if map[new_c[0]][new_c[1]] == val - 1:
                find_path(new_c, origin)



with open("input", "r") as f:
    for l in f:
        map.append([int(i) for i in l.strip()])

start_points = {}
end_points = []

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == 0:
            start_points[(y,x)] = set()
        if map[y][x] == 9:
            end_points.append((y,x))





for p in end_points:
    find_path(p, p)


scores = sum([len(i) for i in start_points.values()])
print(scores)