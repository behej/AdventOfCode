#!/usr/bin/python3



sum = 0

with open("input.txt", "r") as f:
    lines = f.readlines()


for y in range(len(lines)):
    l = lines[y].strip()

    x = 0
    while x < len(l):
        c = l[x]
        # Skip all dots
        if c == '.':
            x += 1
            continue

        is_part_number = False
        if c.isdigit():
            # First digit found, let's parse all digits to get value
            start_pos = x
            val = int(c)
            while x < len(l)-1 and l[x+1].isdigit():
                x +=1
                val = val * 10 + int(l[x])
            end_pos = x
            # All digits have been read

            # Check if special char is found at previous line (watch out list bounds)
            if y > 0:
                for i in range(max(0, start_pos-1), min(len(l)-1, end_pos+1)+1):
                    if not lines[y-1][i].isdigit() and lines[y-1][i] != '.':
                        is_part_number = True

            # Check if special char is found at next line (watch out list bounds)
            if y < len(lines)-1:
                for i in range(max(0, start_pos-1), min(len(l)-1, end_pos+1)+1):
                    if not lines[y+1][i].isdigit() and lines[y+1][i] != '.':
                        is_part_number = True

            # Check special char just before on same line
            if start_pos > 0 and not l[start_pos-1].isdigit() and l[start_pos-1] != '.':
                is_part_number = True

            # Check special char just after on same line
            if end_pos < len(l)-1 and not l[end_pos+1].isdigit() and l[end_pos+1] != '.':
                is_part_number = True

            # Sum value if special char has been found
            if is_part_number:
                sum += val

            x += 1
        x += 1

print(sum)