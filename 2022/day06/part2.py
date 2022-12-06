#! /bin/python3

packet_length = 14


with  open("input", "r") as f:
    message = f.readline().strip()


for i in range(packet_length-1, len(message)):
    header = message[i-packet_length+1:i+1]
    if len(set(header)) == packet_length:
        print(i+1)
        break;
