

def convert_dots_and_hashtags_to_index(ar):
	idx = 0
		
	for i in range(len(ar)):
		if i == 0:
			idx += (1 if ar[-1-i] == "#" else 0)
		else:
			idx += (2 if ar[-1-i] == "#" else 0) ** i
		
	return idx
	


def define_index(input, x, y):
	ar = []

	ar.append(input[y-1][x-1] if ((0 <= (x-1) <= len(input[0])-1) and (0 <= (y-1) <= len(input)-1)) else ".")
	ar.append(input[y-1][x] if ((0 <= (x) <= len(input[0])-1) and (0 <= (y-1) <= len(input)-1)) else ".")
	ar.append(input[y-1][x+1] if ((0 <= (x+1) <= len(input[0])-1) and (0 <= (y-1) <= len(input)-1)) else ".")
	
	ar.append(input[y][x-1] if ((0 <= (x-1) <= len(input[0])-1) and (0 <= (y) <= len(input)-1)) else ".")
	ar.append(input[y][x] if ((0 <= (x) <= len(input[0])-1) and (0 <= (y) <= len(input)-1)) else ".")
	ar.append(input[y][x+1] if ((0 <= (x+1) <= len(input[0])-1) and (0 <= (y) <= len(input)-1)) else ".")
	
	ar.append(input[y+1][x-1] if ((0 <= (x-1) <= len(input[0])-1) and (0 <= (y+1) <= len(input)-1)) else ".")
	ar.append(input[y+1][x] if ((0 <= (x) <= len(input[0])-1) and (0 <= (y+1) <= len(input)-1)) else ".")
	ar.append(input[y+1][x+1] if ((0 <= (x+1) <= len(input[0])-1) and (0 <= (y+1) <= len(input)-1)) else ".")
	
#	ar.append("." if (x <= 0 or y <= 0) else input[y-1][x-1])
#	ar.append("." if (x < 0 or x >= len(input[0])  or y <= 0) else input[y-1][x])
#	ar.append("." if (y <= 0 or x >= (len(input[0]) - 1)) else input[y-1][x+1])
#	
#	ar.append("." if (x <= 0 or y < 0 or y >= len(input)) else input[y][x-1])
#	ar.append("." if (x < 0 or x >= len(input[0]) or y < 0 or y >= len(input)) else input[y][x])
#	ar.append("." if (x >= (len(input[0]) - 1) or y < 0 or y >= len(input)) else input[y][x+1])
#	
#	ar.append("." if (x <= 0 or y >= (len(input) - 1)) else input[y+1][x-1])
#	ar.append("." if (x < 0 or x >= len(input[0])  or y >= (len(input) - 1)) else input[y+1][x])
#	ar.append("." if (x >= (len(input[0]) - 1) or y >= (len(input) - 1)) else input[y+1][x+1])
	
	return convert_dots_and_hashtags_to_index(ar)
	
	
def count_hashtags(image):
	count = 0
	
	for y in range(len(image)):
		for x in range(len(image[y])):
			if image[y][x] == "#":
				count += 1
				
	return count



def enhance_image(input):
	global enhance_algo

	out = []
	for y in range(len(input) + 2):
		out.append([])
		for x in range(len(input[0]) + 2):
			index = define_index(input, x-1, y-1)
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
	



image = enhance_image(image)
image = enhance_image(image)

nb = count_hashtags(image)
print(nb)