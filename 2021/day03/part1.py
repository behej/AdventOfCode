

sum = []	
counter = 0
size = 0



with open("input", "r") as f:
	size = len(f.readline().strip())
	f.seek(0)
	sum = [0]*size
	
		
	for line in f:
		counter += 1
		for (i, c) in zip(range(size), line.strip()[::-1]):
			sum[i] += int(c)
			
print("Number of lines: {}".format(counter))			
print(sum)

threshold = counter/2


gamma = 0
epsilon = 0
for i in range(size):
	if sum[i] > threshold:
		gamma += 2**i
	else:
		epsilon += 2**i
		
		
print("Gamma: {}".format(gamma))
print("Epsilon: {}".format(epsilon))
print("Result: {}".format(gamma*epsilon))
		


		
		
			
			
			
		
		
	