#! /usr/bin/python3



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


file_id -= 1
counter = 0
# Reorganize
while len(free_pos) > 0:
    if counter >= len(files[file_id]):
        file_id -= 1
        counter = 0

    if free_pos[0] < files[file_id][-1-counter]:
        files[file_id][-1-counter] = free_pos[0]
        del(free_pos[0])
    else:
        break
    counter += 1


    
# Compute checksum
sum = 0

for val,l in files.items():
    for i in l:
        sum += val * i

print(sum)