

species = [0]*7
buffer1=0	# Fishes just born (day 1)
buffer2=0	# Fishes 2 days old
buffer3=0   # Fishes 3 days old: will reproduce at same time than next reproduction of today's fishes. Will be added to today's fishes but after they reproduced



with open("input", "r") as f:
	fishes = f.readline().strip().split(",")
	fishes = [int(i) for i in fishes]
	

for f in fishes:
	species[f] += 1

	
	

for d in range(256):

			
	buffer3=buffer2
	buffer2=buffer1
	buffer1=species[d%7]
	species[d%7] += buffer3

print("Number of fishes: {}".format(sum(species)+buffer1+buffer2))
	
