#! /bin/python3

packet_length = [4, 14]

with  open("input", "r") as f:
    message = f.readline().strip()

for (part, packet) in zip(range(len(packet_length)), packet_length):
    for i in range(packet, len(message)+1):
        header = message[i-packet:i]
        if len(set(header)) == packet:
            print("Part {}: {}".format(part+1, i))
            break;
