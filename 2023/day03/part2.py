#!/usr/bin/python3



sum = 0

with open("day03/input.txt", "r") as f:
    lines = f.readlines()


for y in range(len(lines)):
    l = lines[y].strip()

    x = 0
    while x < len(l):
        c = l[x]
        # Skip all what is not stars
        if c != '*':
            x += 1
            continue

        values_around = []

        # Check is value on the right
        if x < len(l)-1 and l[x].isdigit():
            start_pos = x + 1
            val = 0
            while start_pos < len(l)-1 and l[start_pos].isdigit():
                val *= 10
                val += int(l[start_pos])
                start_pos += 1
            values_around.append(val)

        if x > 0 and l[x].isdigit():
            start_pos = x - 1
            digits = []
            while start_pos > 0 and l[start_pos].isdigit():
                digits.append(int(l[start_pos]))
                start_pos -= 1
            digits.reverse()
            val = 0
            for d in digits:
                val = val*10 + d
            values_around.append(val)

        if y > 0 and lines[y-1][x].isdigit():
            # there is only one number above
            start_pos = x
            while start_pos > 0 and lines[y-1][start_pos]
        else:
            # There may be 2 numbers above




   

        x += 1

print(sum)