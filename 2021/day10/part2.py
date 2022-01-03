

score_table = {"(": 1, "[": 2, "{": 3, "<": 4}



def compute_completion_score(l):
	s = 0
	
	for i in range(len(l)-1, -1, -1):
		s *= 5
		s += score_table[l[i]]
		
	return s
		
		
		


score = []

with open("input", "r") as f:
	for l in f:
		l = l.strip()

		sym = []
		corrupted = False

		for c in l:
			if c in "([{<":
				sym.append(c)
			elif c == ")" and sym[-1] == "(":
				sym.pop()
			elif c == "]" and sym[-1] == "[":
				sym.pop()
			elif c == "}" and sym[-1] == "{":
				sym.pop()
			elif c == ">" and sym[-1] == "<":
				sym.pop()
			else:
				# Corrupted line, discard it !
				corrupted = True
				break;
				
		if sym and not corrupted:
		# Sym not empty -> line incomplete
			score.append(compute_completion_score(sym))
		
		
score.sort()
mid_pos = int((len(score)) / 2)

print("Completion score: {}".format(score[mid_pos]))





