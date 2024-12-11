#! /usr/bin/python3


def has_even_digits(n):
    length = len(str(n))
    return (length % 2 == 0)

def split_item(n):
    as_string = str(n)
    length = len(as_string)
    return (int(as_string[:length//2]), int(as_string[length//2:]))


def add_val(d, v, c):
    if v in d.keys():
        d[v] += c
    else:
        d[v] = c

def process(l):
    new_l = {}
    for v,c in l.items():
        if v == 0:
            add_val(new_l, 1, c)
        elif has_even_digits(v):
            (v1, v2) = split_item(v)
            add_val(new_l, v1, c)
            add_val(new_l, v2, c)
        else:
            add_val(new_l, v*2024, c)
        
    return new_l



l = {}

with open("input", "r") as f:
    l = {int(i):1 for i in f.readline().strip().split()}


for i in range(75):
    l = process(l)


print(sum(l.values()))