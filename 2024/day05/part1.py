#! /usr/bin/python3

import math

orders = []
updates = []
total = 0


def find_mid_value(l):
    return l[math.floor(len(l)/2)]


with open("input", "r") as f:
    l = f.readline().strip()
    while l != "":
        orders.append([int(i) for i in l.split("|")])
        l = f.readline().strip()

    for l in f:
        updates.append([int(i) for i in l.strip().split(",")])


for u in updates:
    wrong_order = False
    for o in orders:
        if o[0] in u and o[1] in u:
            if not u.index(o[0]) < u.index(o[1]):
                wrong_order = True
                break
    
    if not wrong_order:
        total += find_mid_value(u)

print(total)