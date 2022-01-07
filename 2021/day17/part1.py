

def find_x_velocity(x):
	v = 0
	sum = 0
	while sum < x:
		v += 1
		sum += v
	return v


def compute_max_height(vel):
	return sum([h for h in range(vel+1)])


# Load file
with  open("input", "r") as f:
	line = f.read().strip()
	x_part = line.split()[2]
	y_part = line.split()[3]
	
	x_part = x_part.split("=")[1].split(",")[0]
	x_range = x_part.split("..")
	x_range = [int(i) for i in x_range]

	y_part = y_part.split("=")[1]
	y_range = y_part.split("..")
	y_range = [int(i) for i in y_range]
	


x_vel_range = [i for i in range(find_x_velocity(x_range[0]), find_x_velocity(x_range[1]) + 1)]

# Maxium height is reached when launched as vertically as possible.
# It will fall vertically to target zone -> horizontal speed will have decreased to 0
# If launched up, speed will decrease until max height, then speed will increase again.
# When passing again to coordinate y=0, speed will have reached initial speed + 1.
# To reach max height, initial speed has to be as high as possible, so does speed when going
# from coord y=0 towards target area. Max possible speed is equal to low point of target area
# (If higher, proble will directly from y=0 to a point below target)
# => max initial speed = lowest point of target - 1
init_y_vel = abs(y_range[0]) - 1


h = compute_max_height(init_y_vel)
print("Maximum height: {}".format(h))


