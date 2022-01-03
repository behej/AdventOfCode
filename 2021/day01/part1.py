
with open("input", "r") as f:
	counter = 0
	prev = 999
	
	for line in f:
		if (int(line) > prev):
			counter += 1
		prev = int(line)
		
print(counter)
	