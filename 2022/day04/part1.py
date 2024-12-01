#! /bin/python3

overlap = 0

with open("input", "r") as f:
    for l in f:
        [elve1, elve2] = l.split(",")
        [min1, max1] = elve1.split("-")
        [min2, max2] = elve2.split("-")

        [min1, max1, min2, max2] = [int(i) for i in [min1, max1, min2, max2]]

        if (min2 >= min1 and max2 <= max1) or (min1 >= min2 and max1 <= max2):
            overlap += 1

print(overlap)
