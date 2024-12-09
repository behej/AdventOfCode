#! /usr/bin/python3


def find_contiguous_free_space(l):
    if l == 1:
        return 0

    counter = 1
    for i in range(1, len(free_pos)):
        if free_pos[i] - free_pos[i-1] == 1:
            counter += 1
            if counter >= l:
                return i-l+1
        else:
            counter = 1


    # alternative
    # for i in range(len(free_pos) - l):
    #     if free_pos[i+l] == free_pos[i] + l:
    #         return i
        
    return -1




with open("input", "r") as f:
    l = f.readline().strip()


file_not_free = True
file_id = 0
files = {}
disk_pos = 0
free_pos = []

for c in l:
    if file_not_free:
        files[file_id] = list(range(disk_pos, disk_pos + int(c)))
        file_id += 1
        file_not_free = False        
    else:
        free_pos += range(disk_pos, disk_pos + int(c))
        file_not_free = True
    disk_pos += int(c)


# Reorganize
file_id -= 1
counter = 0
for f in range(file_id, -1, -1):
    length = len(files[f])

    pos = find_contiguous_free_space(length)
    if 0 <= pos and free_pos[pos] < files[f][0]:
        for i in range(length):
            files[f][i] = free_pos[pos]
            del(free_pos[pos])

    
# Compute checksum
sum = 0
for val,l in files.items():
    for i in l:
        sum += val * i

print(sum)