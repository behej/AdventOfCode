#! /usr/bin/python3

def move(pos, cmd):
    if cmd == '^':
        return (pos[0], pos[1]+1)
    elif cmd == 'v':
        return (pos[0], pos[1]-1)
    elif cmd == '<':
        return (pos[0]-1, pos[1])
    elif cmd == '>':
        return (pos[0]+1, pos[1])
            
            
input = open("input", "r").readline()

santa = (0, 0)
robot = (0, 0)
visited = [santa]

for cmd1, cmd2 in zip(input[::2], input[1::2]):
    santa = move(santa, cmd1)
    robot = move(robot, cmd2)
        
    if santa not in visited:
        visited.append(santa)
    if robot not in visited:
        visited.append(robot)
    
    
print(len(visited))
