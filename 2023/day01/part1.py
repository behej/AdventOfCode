#!/usr/bin/python3


def char2number(c):
    return ord(c) - ord('0')



sum = 0
with open("input.txt", "r") as f:
    for l in f:
        digits = [c for c in l if c.isdigit()]
        value = char2number(digits[0]) * 10 + char2number(digits[-1])
        sum += value

print(sum)