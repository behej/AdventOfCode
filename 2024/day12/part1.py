#! /usr/bin/python3



def scan(l, c, visited):
    perim = 0
    surf = 1

    l.remove(c)
    visited.append(c)

    for i,j in [(-1,0), (1,0), (0,-1), (0,1)]:
        if (c[0] + i, c[1] + j) in l:
            new_p, new_s = scan(l, (c[0] +i, c[1] + j), visited)
            perim += new_p
            surf += new_s
        elif (c[0] + i, c[1] + j) not in visited:
            perim += 1



    return perim, surf
    


temp = []
with open("input", "r") as f:
    for l in f:
        temp.append(l.strip())
    

map = {}
for (y,l) in enumerate(temp):
    for (x,c) in enumerate(l):
        if c in map:
            map[c].append((y,x))
        else:
            map[c] = [(y,x)]



result = 0

for coords in map.values():
    while coords:
        perim, surf = scan(coords, coords[0], visited=[])
        result += (perim * surf)


print(result)



    



