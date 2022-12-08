#! /usr/bin/python3

with open("input", "r") as f:
    rows = [l.strip() for l in f]


count = 0

for i in range(1, len(rows)-1):
    for j in range(1, len(rows[i])-1):
        height = int(rows[i][j])

        west = [int(k) for k in rows[i][:j]]
        east = [int(k) for k in rows[i][j+1:]]
        north = [int(rows[k][j]) for k in range(i)]
        south = [int(rows[k][j]) for k in range(i+1, len(rows))]

        west.sort(reverse=True)
        east.sort(reverse=True)
        south.sort(reverse=True)
        north.sort(reverse=True)

        if west[0] < height:
            count += 1
        elif east[0] < height:
            count += 1
        elif south[0] < height:
            count += 1
        elif north[0] < height:
            count += 1


total = count + 2*len(rows) + 2*len(rows[0]) - 4

print(total)
