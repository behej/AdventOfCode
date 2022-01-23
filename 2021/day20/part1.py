

def convert_dots_and_hashtags_to_index(ar):
	idx = 0
		
	for i in range(len(ar)):
		if i == 0:
			idx += (1 if ar[-1-i] == "#" else 0)
		else:
			idx += (2 if ar[-1-i] == "#" else 0) ** i
		
	return idx
	


def define_index(input, x, y, off_grid_pixel):
	ar = []

	ar.append(input[y-1][x-1] if ((0 <= (x-1) <= len(input[0])-1) and (0 <= (y-1) <= len(input)-1)) else off_grid_pixel)
	ar.append(input[y-1][x] if ((0 <= (x) <= len(input[0])-1) and (0 <= (y-1) <= len(input)-1)) else off_grid_pixel)
	ar.append(input[y-1][x+1] if ((0 <= (x+1) <= len(input[0])-1) and (0 <= (y-1) <= len(input)-1)) else off_grid_pixel)
	
	ar.append(input[y][x-1] if ((0 <= (x-1) <= len(input[0])-1) and (0 <= (y) <= len(input)-1)) else off_grid_pixel)
	ar.append(input[y][x] if ((0 <= (x) <= len(input[0])-1) and (0 <= (y) <= len(input)-1)) else off_grid_pixel)
	ar.append(input[y][x+1] if ((0 <= (x+1) <= len(input[0])-1) and (0 <= (y) <= len(input)-1)) else off_grid_pixel)
	
	ar.append(input[y+1][x-1] if ((0 <= (x-1) <= len(input[0])-1) and (0 <= (y+1) <= len(input)-1)) else off_grid_pixel)
	ar.append(input[y+1][x] if ((0 <= (x) <= len(input[0])-1) and (0 <= (y+1) <= len(input)-1)) else off_grid_pixel)
	ar.append(input[y+1][x+1] if ((0 <= (x+1) <= len(input[0])-1) and (0 <= (y+1) <= len(input)-1)) else off_grid_pixel)
	
	
	return convert_dots_and_hashtags_to_index(ar)
	
	
def count_hashtags(image):
	count = 0
	
	for y in range(len(image)):
		for x in range(len(image[y])):
			if image[y][x] == "#":
				count += 1
				
	return count



def enhance_image(input, off_grid_pixel_state):
	global enhance_algo
	
	
	out = []
	for y in range(len(input) + 2):
		out.append([])
		for x in range(len(input[0]) + 2):
			index = define_index(input, x-1, y-1, off_grid_pixel=off_grid_pixel_state)
			out[y].append(enhance_algo[index])
			
	return out





image = []



# Load file
with  open("input", "r") as f:
	enhance_algo = f.readline().strip()
	
	# Skip empty line
	f.readline()
	
	for l in f:
		image.append(l.strip())
	

invisible_pixel = "."

for i in range(2):
	image = enhance_image(image, invisible_pixel)
	invisible_pixel = enhance_algo[0] if invisible_pixel == "." else enhance_algo[-1]


nb = count_hashtags(image)
print("Pixels lit: {}".format(nb))