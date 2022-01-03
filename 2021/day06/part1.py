
fishes = []

with open("input", "r") as f:
	fishes = f.readline().strip().split(",")
	fishes = [int(i) for i in fishes]
	

for i in range(80):
	for i in range(len(fishes)):
		if fishes[i] == 0:
			fishes.append(8)
			fishes[i] = 6
		else:
			fishes[i] -= 1


print("Number of fishes: {}".format(len(fishes)))
