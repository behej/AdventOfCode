

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
	
# Min horizontal velocity to reach left edge
x_vel_min = find_x_velocity(x_range[0])

# Max horizontal velocity (higher, we will overshoot right edge at 1st step)
x_vel_max = x_range[1]

# Max vertical velocity: Shoot as vertical as possible (see explanations on part 1)
y_vel_max = abs(y_range[0]) - 1

# Min vertical velocity: Shoot downwards, directly towards the target (Higher speed will overshoot target at 1st step)
y_vel_min = y_range[0]



valid_velocities = []

for x in range(x_vel_min, x_vel_max+1):
	for y in range(y_vel_min, y_vel_max+1):
		p = (0, 0)
		v = (x, y)
		while True:
			p = (p[0]+v[0], p[1]+v[1])
			v = (v[0]-1 if v[0] > 0 else 0, v[1]-1)
			
			# Position in target area
			if (x_range[0] <= p[0] <= x_range[1]) and (y_range[0] <= p[1] <= y_range[1]):
				valid_velocities.append((x, y))
				break
				
			# Probe will never reach target
			# - horizontal velocity is null and position still left from target
			# - horizontal position has overpassed target
			# - vertical position is below target
			if (v[0] == 0 and p[0] < x_range[0]) or (p[0] > x_range[1]) or (p[1] < y_range[0]):
				break


print("Number of initial velocities that will reach target: {}".format(len(valid_velocities)))



