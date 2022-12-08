#! /usr/bin/python3


def compute_scenic(h, n, s, e, w):
    score = 1
    n.reverse()
    w.reverse()

    for direction in [n, s, e, w]:
        try:
            tree = next(x for x in direction if x >= h)
            score *= (direction.index(tree) + 1)
        except StopIteration:
            score *= len(direction)

    return score




with open("input", "r") as f:
    rows = [l.strip() for l in f]


max_score = 0

for i in range(1, len(rows)-1):
    for j in range(1, len(rows[i])-1):
        height = int(rows[i][j])

        west = [int(k) for k in rows[i][:j]]
        east = [int(k) for k in rows[i][j+1:]]
        north = [int(rows[k][j]) for k in range(i)]
        south = [int(rows[k][j]) for k in range(i+1, len(rows))]

        score = compute_scenic(height, north, south, east, west)
        max_score = max(max_score, score)


print(max_score)
