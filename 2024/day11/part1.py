#! /usr/bin/python3


def has_even_digits(n):
    length = len(str(n))
    return (length % 2 == 0)

def split_item(n):
    as_string = str(n)
    length = len(as_string)
    return [int(as_string[:length//2]), int(as_string[length//2:])]

def process(l):
    for i in range(len(l)):
        if isinstance(l[i], list):
            process(l[i])
        else:
            if l[i] == 0:
                l[i] = 1
            elif has_even_digits(l[i]):
                l[i] = split_item(l[i])
            else:
                l[i] *= 2024

def count_stones(l):
    sum = 0
    for i in l:
        if isinstance(i,list):
            sum += count_stones(i)
        else:
            sum += 1

    return sum

l = []

with open("input", "r") as f:
    l = [int(i) for i in f.readline().strip().split()]


print(l)

for _ in range(25):
    process(l)


sum = count_stones(l)
print(sum)