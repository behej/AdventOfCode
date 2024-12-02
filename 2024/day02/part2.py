#! /usr/bin/python3


safe_levels = 0

def is_valid(l):
    dir = 1 if l[0] < l[1] else -1

    for i in range(len(l) - 1):
        if not(0 < ((l[i+1] - l[i]) * dir) <= 3):
            return i
        
    return -1


with open("input", "r") as f:
    for line in f:
        l = [int(i) for i in line.split()]


        code = is_valid(l)
        if code == -1:
            safe_levels += 1
            continue

        l2 = l.copy()
        del(l2[code])
        if is_valid(l2) == -1:
            safe_levels += 1
            continue
        
        l2 = l.copy()
        del(l2[code + 1])
        if is_valid(l2) == -1:
            safe_levels += 1
            continue

        del(l[0])
        if is_valid(l) == -1:
            safe_levels += 1
            continue
            


print(safe_levels)