from itertools import product

cubes = {}


# Load file
with  open("input", "r") as f:
	for l in f:
		state = l.strip().split()[0]
		x_range = l.strip().split()[1].split(",")[0].split("=")[1]
		y_range = l.strip().split()[1].split(",")[1].split("=")[1]
		z_range = l.strip().split()[1].split(",")[2].split("=")[1]
	
		x_min = int(x_range.split("..")[0])
		x_max = int(x_range.split("..")[1])
		y_min = int(y_range.split("..")[0])
		y_max = int(y_range.split("..")[1])
		z_min = int(z_range.split("..")[0])
		z_max = int(z_range.split("..")[1])
		
	
		
		for (x, y, z) in product(range(x_min, x_max+1), range(y_min, y_max+1), range(z_min, z_max+1)):
			cubes[(x, y, z)] = 1 if state == "on" else 0
				
		
print(sum(cubes.values()))
