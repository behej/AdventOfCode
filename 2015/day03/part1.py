#! /usr/bin/python3

input = open("input", "r").readline()

c = (0, 0)
visited = [c]

for cmd in input:
    if cmd == '^':
        c = (c[0], c[1]+1)
    elif cmd == 'v':
        c = (c[0], c[1]-1)
    elif cmd == '<':
        c = (c[0]-1, c[1])
    elif cmd == '>':
        c = (c[0]+1, c[1])
        
    if c not in visited:
        visited.append(c)

print(len(visited))
    