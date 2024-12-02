#! /usr/bin/python3


safe_levels = 0


with open("input", "r") as f:
    for line in f:
        l = [int(i) for i in line.split()]


        dir = 1 if l[0] < l[1] else -1

        valid = True
        for i in range(len(l) - 1):
            if not(0 < ((l[i+1] - l[i]) * dir) <= 3):
                valid = False
                break
        if valid:
            safe_levels += 1


print(safe_levels)
