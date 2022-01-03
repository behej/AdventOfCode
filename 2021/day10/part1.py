


def compute_score(c):
	if c == ")":
		return 3
	elif c == "]":
		return 57
	elif c == "}":
		return 1197
	elif c == ">":
		return 25137
	else:
		return 0




score = 0

with open("input", "r") as f:
	for l in f:
		l = l.strip()

		sym = []

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
				score += compute_score(c)
				break;



print("Syntax error score: {}".format(score))





