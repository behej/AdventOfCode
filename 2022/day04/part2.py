#! /bin/python3

overlap = 0

with open("input", "r") as f:
    for l in f:
        [elve1, elve2] = l.split(",")
        [min1, max1] = elve1.split("-")
        [min2, max2] = elve2.split("-")

        [min1, max1, min2, max2] = [int(i) for i in [min1, max1, min2, max2]]

        if (min1 in range(min2, max2+1)) or (max1 in range(min2, max2+1)) \
            or (min2 in range(min1, max1+1)) or (max2 in range(min1, max1+1)):
            overlap += 1

print(overlap)
