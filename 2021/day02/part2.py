
aim = 0
pos = 0
depth = 0

with open("input", "r") as f:
	for line in f:
		cmd = line.split(" ")[0]
		value = int(line.split(" ")[1])
		
		if (cmd == "forward"):
			pos += value
			depth += value * aim
		elif (cmd == "up"):
			aim -= value
		elif (cmd == "down"):
			aim += value
		else:
			print("Unknown command")
			
			
print("Position: {}".format(pos))
print("Depth: {}".format(depth))
print("Result: {}".format(pos*depth))		
		
		
		
	