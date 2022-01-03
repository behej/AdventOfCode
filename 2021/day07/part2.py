

def fuel_consumption(distance):
	return sum(range(distance+1))



crabs = []

with open("input", "r") as f:
	crabs = f.readline().strip().split(",")
	crabs = [int(i) for i in crabs]
	
crabs = sorted(crabs)

min_fuel = 999999999

for p in range(crabs[0], crabs[-1]):
	fuel = 0
	
	for c in crabs:
		fuel += (fuel_consumption(abs(p-c)))
		if (fuel >= min_fuel):
			break
			
	if (fuel < min_fuel):
		min_fuel = fuel
		


print("Minimum fuel required: {}".format(min_fuel))

