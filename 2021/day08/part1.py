
count = 0


with open("input", "r") as f:
	for l in f:
		digits = l.strip().split("|")[1].strip().split()
		
		for d in digits:
			if len(d) in [2, 3, 4, 7]:
				count += 1
				
print("Number of 1, 4, 7 or 8: {}".format(count))


