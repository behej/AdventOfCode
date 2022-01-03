

def fold_along_x(dot, axis):
	x = dot[0]
	y = dot[1]
	
	x = (2 * axis - x) if x > axis else x
	return (x, y)
	


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
			

f = folds[0]

if f[0] == "x":
	dots = [fold_along_x(d, f[1]) for d in dots]
elif f[0] == "y":
	fold_along_y(f[1])
else:
	print("Wrong fold instruction")


	
# remove duplicates
dots = list(set(dots))


print("Visible dots: {}".format(len(dots)))


