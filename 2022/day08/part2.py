#! /usr/bin/python3

def compute_scenic(height, *directions):
    score = 1
    for direction in directions:
        score *= next((index+1 for index, x in enumerate(direction) if x >= h), len(direction))

    return score


with open("input", "r") as f:
    rows = [l.strip() for l in f]

max_score = 0
for i in range(0, len(rows)):
    for j in range(0, len(rows[i])):
        h = int(rows[i][j])

        west = list(reversed([int(k) for k in rows[i][:j]]))
        east = [int(k) for k in rows[i][j+1:]]
        north = list(reversed([int(rows[k][j]) for k in range(i)]))
        south = [int(rows[k][j]) for k in range(i+1, len(rows))]

        score = compute_scenic(h, north, south, east, west)
        max_score = max(max_score, score)


print(max_score)
