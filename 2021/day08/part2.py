
# Identify each number
def identify_numbers(raw_numbers):
	wires = {}
	decoded_numbers = []

	numbers_with_five_segs = find_five_segs(raw_numbers)
	numbers_with_six_segs = find_six_segs(raw_numbers)

	one = find_one(raw_numbers)
	four = find_four(raw_numbers)
	seven = find_seven(raw_numbers)
	eight = find_eight(raw_numbers)
	three = find_three(numbers_with_five_segs, one)
	wires['a'] = find_wire_a(one, seven)
	wires['g'] = find_wire_g(three, four, wires['a'])
	wires['b'] = find_wire_b(three, four)
	wires['d'] = find_wire_d(four, one, wires['b'])
	zero = find_zero(numbers_with_six_segs, wires['d'])
	two = find_two(numbers_with_five_segs, three, wires['b'])
	five = find_five(numbers_with_five_segs, three, wires['b'])
	wires['c'] = find_wire_c(five, one)
	six = find_six(numbers_with_six_segs, wires['c'])
	nine = find_nine(numbers_with_six_segs, zero, six)
	
	decoded_numbers = [
		(zero, 0),
		(one, 1),
		(two, 2),
		(three, 3),
		(four, 4),
		(five, 5),
		(six, 6),
		(seven, 7),
		(eight, 8),
		(nine, 9)
	]
	
	return decoded_numbers
	

def decode(input, key):
	res = []

	for d in input:
		for k in key:
			if sorted(d) == k[0]:
				res.append(k[1])
				break
	return res
	

def digit_to_decimal(digits):
	value = 0
	n = len(digits)
	for i in range(n):
		value += digits[n-i-1] * 10**i


	return value


# Find numbers
def find_zero(six_segs, wire_d):
	return [n for n in six_segs if not set([wire_d]).issubset(n)][0]
	

def find_one(numbers):
	return sorted([n for n in numbers if len(n) == 2][0])

def find_two(five_segs, three, wire_b):
	return [n for n in five_segs if (not set(three).issubset(n) and not set([wire_b]).issubset(n))][0]

def find_three(five_segs, one):
	return [n for n in five_segs if set(one).issubset(n)][0]

def find_four(numbers):
	return sorted([n for n in numbers if len(n) == 4][0])

def find_five(five_segs, three, wire_b):
	return [n for n in five_segs if (not set(three).issubset(n) and set([wire_b]).issubset(n))][0]

def find_six(six_segs, wire_c):
	return [n for n in six_segs if not set([wire_c]).issubset(n)][0]

def find_seven(numbers):
	return sorted([n for n in numbers if len(n) == 3][0])
	
def find_eight(numbers):
	return sorted([n for n in numbers if len(n) == 7][0])
	
def find_nine(six_segs, zero, six):
	return [n for n in six_segs if (not set(zero).issubset(n) and not set(six).issubset(n))][0]

# Find numers with segs
def find_five_segs(numbers):
	collec = [n for n in numbers if len(n) == 5]
	return [sorted(c) for c in collec]
	
def find_six_segs(numbers):
	collec = [n for n in numbers if len(n) == 6]
	return [sorted(c) for c in collec]

# Find wires
def find_wire_a(one, seven):
	return list(set(seven) - set(one))[0]
	
def find_wire_c(five, one):
	return list(set(one) - set(five))[0]
	
def find_wire_g(three, four, wire_a):
	return list(set(three) - set(four) - set([wire_a]))[0]
	
def find_wire_b(three, four):
	return list(set(four) - set(three))[0]
 
def find_wire_d(four, one, wire_b):
	return list(set(four) - set(one) - set([wire_b]))[0]
 
 
#############################################################


total = 0

with open("input", "r") as f:
	for l in f:
		part1 = l.strip().split("|")[0].strip()
		part2 = l.strip().split("|")[1].strip()
		
		raw_numbers = part1.split()
		digits_to_decode = part2.split()
		
		decode_key = identify_numbers(raw_numbers)
		decoded_digits = decode(digits_to_decode, decode_key)
		value = digit_to_decimal(decoded_digits)
		total += value


print("Total: {}".format(total))



# wires = {}
# 
# 
# numbers_with_five_segs = find_five_segs(numbers)
# numbers_with_six_segs = find_six_segs(numbers)
# 
# one = find_one(numbers)
# four = find_four(numbers)
# seven = find_seven(numbers)
# eight = find_eight(numbers)
# three = find_three(numbers_with_five_segs, one)
# wires['a'] = find_wire_a(one, seven)
# wires['g'] = find_wire_g(three, four, wires['a'])
# wires['b'] = find_wire_b(three, four)
# wires['d'] = find_wire_d(four, one, wires['b'])
# zero = find_zero(numbers_with_six_segs, wires['d'])
# two = find_two(numbers_with_five_segs, three, wires['b'])
# five = find_five(numbers_with_five_segs, three, wires['b'])
# wires['c'] = find_wire_c(five, one)
# six = find_six(numbers_with_six_segs, wires['c'])
# nine = find_nine(numbers_with_six_segs, zero, six)
# 
# 
# print(wires)
# print("Zero: {}".format(zero))
# print("One: {}".format(one))
# print("Two: {}".format(two))
# print("Three: {}".format(three))
# print("Four: {}".format(four))
# print("Five: {}".format(five))
# print("Six: {}".format(six))
# print("Seven: {}".format(seven))
# print("Eight: {}".format(eight))
# print("Nine: {}".format(nine))
# 

#   
#   
#   
#   1  = 2
#   2 = 5
#   3  = 5
#   4 =  4
#   5 = 5
#   6 = 6
#   7 = 3
#   8 = 7
#   9 = 6
#   0 = 6
#   
#   
#   2 seg: 1
#   3 seg: 7
#   4 seg: 4
#   5 seg: 2, 3, 5
#   6 seg: 6, 9, 0
#   7 seg: 8
#   
#   0: si 6 seg ET ceux du 1 ET PAS ceux restant du 4
#   1: 2 only
#   2: si 5 seg ET pas ceux du 1 ET pas ceux restant du 4
#   3: si 5 seg et les 2 du 1
#   4: 4 only
#   5: si 5 seg ET pas ceux de 1 ET ceux restant du 4
#   6: si 6 seg ET pas ceux du 1 ET ceux restant du 4
#   7: 3 only
#   8: 7 only
#   9: si 6 seg  ET ceux restant du 4
#   
#   
#   
#   ===============
#   1 - cg
#   7 - acg
#   4 - cdfg
#   2 - abefg
#   3 - acefg
#   5 - acdef
#   0 - abcdeg 09
#   6 - abcdef
#   9 - acdefg 09
#   8 - abcdefg
#   ============
#   | fabgced gc agc cdfg
#   
#   
#   bgafcde   ebdgac adfceb bafeg efgca cgdfae ecadf | fabgced   
#   
#   1: cg
#   7: acg -> a=a
#	3: acefg
#   4: cdfg  -> leftpart=df
	
# 	g : e

#   5 digits: abefg acefg acdef
#   
#   