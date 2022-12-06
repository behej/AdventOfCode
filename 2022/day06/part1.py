#! /bin/python3

with  open("input", "r") as f:
    message = f.readline().strip()


for i in range(3, len(message)):
    header = message[i-3:i+1]
    if len(set(header)) == 4:
        print(i+1)
        break;
