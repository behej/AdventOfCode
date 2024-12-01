#!/usr/bin/python3


sum = 0

with open("day02/input.txt", "r") as f:
    for l in f:
        mins = {'red' : 0, 'green': 0, 'blue': 0}
        l = l.split(':')[1].strip()

        for set in l.split(';'):
            for reveal in set.split(','):
                c = reveal.strip().split(' ')[1]
                q = int(reveal.strip().split(' ')[0])

                mins[c] = max(mins[c], q)
            
        power = mins['red'] * mins['green'] * mins['blue']
        sum += power

           
print(sum)