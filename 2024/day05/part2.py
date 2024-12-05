#! /usr/bin/python3

import math

orders = []
updates = []
total = 0


def find_mid_value(l):
    return l[math.floor(len(l)/2)]

def is_ordered(l):
    for o in orders:
        if o[0] in l and o[1] in l:
            if not l.index(o[0]) < l.index(o[1]):
                return False
    return True


def reorder(l):
    for i in range(len(l) - 1):
        for o in orders:
            if l[i] == o[1] and l[i+1] == o[0]:
                l[i], l[i+1] = l[i+1], l[i]

    if not is_ordered(l):
        reorder(l)

    return l

            



with open("input", "r") as f:
    l = f.readline().strip()
    while l != "":
        orders.append([int(i) for i in l.split("|")])
        l = f.readline().strip()

    for l in f:
        updates.append([int(i) for i in l.strip().split(",")])


for u in updates:
    if not is_ordered(u):
        u = reorder(u)
        total += find_mid_value(u)

print(total)