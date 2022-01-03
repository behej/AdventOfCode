


def insert_elements(list_A, list_B):
	tmp_list = list_A + list(reversed(list_B))
	return [(tmp_list[int(i/2)] if not i%2 else tmp_list[int(len(tmp_list)-1-(i-1)/2)]) for i in range(len(tmp_list))]


def count_occurences(l):
	occ = {}

	for item in l:
		if item in occ.keys():
			occ[item] += 1
		else:
			occ[item] = 1

	return occ



template = ""
rules = {}


with  open("input", "r") as f:
	for l in f:
		# Skip empty lines
		if not l.strip():
			continue
			
		# Pair insertion rules
		if "->" in l:
			rules[l.strip().split("->")[0].strip()] = l.strip().split("->")[1].strip()
		
		# Polymer template
		else:
			template = list(l.strip())
			


for loop in range(10):
	to_insert = []
	for i in range(len(template)-1):
		key = template[i] + template[i+1]
		to_insert.append(rules[key])

	template = insert_elements(template, to_insert)

counts = count_occurences(template)

most = sorted(counts.values())[-1]
least = sorted(counts.values())[0]

print("Most common: {} - least common: {} = {}".format(most, least, most - least))