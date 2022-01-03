import numpy as np

def fold_along_x(dot, axis):
	x = dot[0]
	y = dot[1]
	
	x = (2 * axis - x) if x > axis else x
	return (x, y)


def fold_along_y(dot, axis):
	x = dot[0]
	y = dot[1]
	
	y = (2 * axis - y) if y > axis else y
	return (x, y)

def find_dimensions(dots):
	max_x = 0
	max_y = 0
	
	for d in dots:
		max_x = d[0] if d[0] > max_x else max_x
		max_y = d[1] if d[1] > max_y else max_y
	
	return (max_x+1, max_y+1)


def dots_to_bmp(dots):
	string = ""
	(max_x, max_y) = find_dimensions(dots)
	
	A = np.full((max_y, max_x), fill_value=" ")
	for (x,y) in dots:
		A[y,x] = "#"
	
	
	for y in range(A.shape[0]):
		for x in range(A.shape[1]):
			string += A[y,x]
		string += "\n"
	
	return string


dots = []
folds = []


with  open("input", "r") as f:
	for l in f:
		# Skip empty lines
		if not l.strip():
			continue
			
		# Fold instructions
		if l.startswith("fold"):
			instr = l.strip().split(" ")[-1].split("=")
			folds.append((instr[0], int(instr[1])))
		
		# Dots coordinates
		else:
			coord = l.strip().split(",")
			coord = [int(c) for c in coord]
			dots.append((coord[0], coord[1]))
			
for f in folds:
	if f[0] == "x":
		dots = [fold_along_x(d, f[1]) for d in dots]
	elif f[0] == "y":
		dots = [fold_along_y(d, f[1]) for d in dots]
	else:
		print("Wrong fold instruction")
		
	# remove duplicates
	dots = list(set(dots))


rendering = dots_to_bmp(dots)

print(rendering)


