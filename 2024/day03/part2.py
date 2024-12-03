#! /usr/bin/python3


import re



def compute_val(txt):
    sum = 0
    for i in re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", txt):
        sum += int(i[4:-1].split(",")[0]) * int(i[4:-1].split(",")[1])

    return sum


total = 0
text = ""
with open("input", "r") as f:
    do_dont_s = re.split("do\(\)", f.read())

    for do_dont in do_dont_s:
        do_s = re.split("don't\(\)", do_dont)[0]
        total += compute_val(do_s)


print(total)


