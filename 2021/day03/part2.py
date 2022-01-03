

listForGamma = []
listForEpsilon = []

with open("input", "r") as f:
	for line in f:
		listForGamma.append(line.strip())

listForEpsilon = list(listForGamma)
		
filterGamma = ""
filterEpsilon = ""

print("Searching Gamma")
print("===============")

for pos in range(len(listForGamma[0])):
	
	# Parsing list for Gamma
	counter = 0
	for item in listForGamma:
		counter += int(item[pos])
		
	if (counter >= len(listForGamma)/2):
		filterGamma += "1"
	else:
		filterGamma += "0"
		
	print("New filter: {}".format(filterGamma))
	print("Before filtering: {} items".format(len(listForGamma)))
		
	listForGamma = [it for it in listForGamma if it.startswith(filterGamma)]
	print("After filtering: {} items".format(len(listForGamma)))
	print("")
	
	if (len(listForGamma) == 1):
		print("Gamma value found after {} iterations".format(pos))
		break;
	
	
print("Searching Epsilon")
print("=================")


for pos in range(len(listForEpsilon[0])):
		
	# Parsing list for Epsion
	counter = 0
	for item in listForEpsilon:
		counter += int(item[pos])
		
	if (counter >= len(listForEpsilon)/2):
		filterEpsilon += "0"
	else:
		filterEpsilon += "1"
		
	print("New filter: {}".format(filterEpsilon))
	print("Before filtering: {} items".format(len(listForEpsilon)))
	
	listForEpsilon = [it for it in listForEpsilon if it.startswith(filterEpsilon)]
	print("After filtering: {} items\n".format(len(listForEpsilon)))
	
	
	
	if (len(listForEpsilon) == 1):
		print("Epsilon value found after {} iterations".format(pos))
		break;
	
gammaBin = listForGamma[0]
epsilonBin = listForEpsilon[0]

print("Gamma = {}".format(gammaBin))
print("Epsilon = {}".format(epsilonBin))

gamma = 0
epsilon = 0
	
for (i,c) in zip(range(len(gammaBin)), gammaBin[::-1]):
	gamma += int(c) * (2**i)
	
for (i,c) in zip(range(len(epsilonBin)), epsilonBin[::-1]):
	epsilon += int(c) * (2**i)
	
print("Gamma = {}".format(gamma))
print("Epsilon = {}".format(epsilon))
	
	
print("Result = {}".format(gamma*epsilon))

