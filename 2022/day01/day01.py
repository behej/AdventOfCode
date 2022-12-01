#! /bin/python3

calories = []

with open("input", "r") as f:
    calories.append(0)
    for l in f:
        if not l.isspace():
            calories[-1] += int(l)
        else:
            calories.append(0)

calories.sort(reverse=True)


print("Part 1: {}".format(calories[0]))
print("Part 2: {}".format(calories[0] + calories[1] + calories[2]))


