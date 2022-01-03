
crabs = []

with open("input", "r") as f:
	crabs = f.readline().strip().split(",")
	crabs = [int(i) for i in crabs]
	

crabs = sorted(crabs)

target = crabs[int(len(crabs)/2)]
print("Target position: {}".format(target))


fuel = 0
for c in crabs:
	fuel += (abs(target-c))


print("Total fuel required: {}".format(fuel))

