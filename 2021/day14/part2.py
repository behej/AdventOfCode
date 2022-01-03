from collections import Counter

template = ""
rules = {}


# Load file
with  open("input", "r") as f:
	for l in f:
		# Skip empty lines
		if not l.strip():
			continue
			
		# Pair insertion rules
		if "->" in l:
			pair_in = l.strip().split("->")[0].strip()
			elem = l.strip().split("->")[1].strip()
			pair_out_1 = pair_in[0] + elem
			pair_out_2 = elem + pair_in[1]
		
			rules[pair_in] = (pair_out_1, pair_out_2)
		
		# Polymer template
		else:
			template = list(l.strip())
			

# Get list of pairs from file
pairs = Counter()
for i in range(len(template)-1):
	pairs[template[i] + template[i+1]] += 1


# Iterate 40 times to create new pairs
for i in range(40):
	new_pairs = Counter()
	for (p,c) in pairs.items():
		new_pairs[rules[p][0]] += c
		new_pairs[rules[p][1]] += c

	pairs = new_pairs


# Count elements present in pairs
#================================
# Each element is counted twice as present in 2 pairs. Need to divide qty by 2
counts = Counter()
for (p,c) in pairs.items():
	counts[p[0]] += c/2
	counts[p[1]] += c/2

# First and last element not counted twice, correct qty for these 2 elements
counts[template[0]] += 1/2
counts[template[-1]] += 1/2

# Most and least common elements
most = int(counts.most_common(1)[0][1])
least = int(counts.most_common()[-1][1])

print("Most common: {} - least common: {} = {}".format(most, least, most - least))