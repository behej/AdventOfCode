#! /usr/bin/python3

def move_head(dir):
    global head
    if dir == 'L':
        head = (head[0]-1, head[1])
    elif dir == 'R':
        head = (head[0]+1, head[1])
    elif dir == 'U':
        head = (head[0], head[1]+1)
    elif dir == 'D':
        head = (head[0], head[1]-1)



def move_tail():
    global head
    global tail

    if (head[0]-1 <= tail[0] <= head[0]+1) and \
        (head[1]-1 <= tail[1] <= head[1]+1):
        # No move
        pass
    else:
        # move
        if (head[1] > tail[1]):
            tail = (tail[0], tail[1]+1)
        if (head[1] < tail[1]):
            tail = (tail[0], tail[1]-1)
        if (head[0] > tail[0]):
            tail = (tail[0]+1, tail[1])
        if (head[0] < tail[0]):
            tail = (tail[0]-1, tail[1])

def register_tail():
    if tail not in visited:
        visited.append(tail)



visited = []
head = (0, 0)
tail = (0, 0)


with open("input", "r") as f:
    for l in f:
        for i in range(int(l.split()[1])):
            move_head(dir=l.split()[0])
            move_tail()
            register_tail()


print(len(visited))
