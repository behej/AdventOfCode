
pos = 0
depth = 0

with open("input", "r") as f:
	for line in f:
		cmd = line.split(" ")[0]
		value = line.split(" ")[1]
		
		if (cmd == "forward"):
			pos += int(value)
		elif (cmd == "up"):
			depth -= int(value)
		elif (cmd == "down"):
			depth += int(value)
		else:
			print("Unknown command")
			
			
print("Position: {}".format(pos))
print("Depth: {}".format(depth))
print("Result: {}".format(pos*depth))		
		
		
		
	