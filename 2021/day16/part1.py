
class Packet:
	def __init__(self, seq):
		self.children = []
		self.value = 0
		self.version = bits_to_int(seq[:3])
		del(seq[:3])
		self.type = bits_to_int(seq[:3])
		del(seq[:3])

		# Packet is a value
		if self.type == 4:
			val_array = []
			while seq[0]:
				del(seq[0])
				val_array += seq[:4]
				del(seq[:4])
			del(seq[0])
			val_array += seq[:4]
			del(seq[:4])
			self.value = bits_to_int(val_array)
			
		# Packet is an operation (contains subpackets)	
		else:
			self.length_type = seq[0]
			del(seq[0])
			# Length_type = True -> length = number of subpackets
			if self.length_type:
				self.length = bits_to_int(seq[:11])
				del(seq[:11])
			# Length type = False -> length = num of bits
			else:
				self.length = bits_to_int(seq[:15])
				del(seq[:15])
				initial_len = len(seq)
			
			while (self.length_type and len(self.children) < self.length) or (not self.length_type and initial_len-len(seq) < self.length):
				self.children.append(Packet(seq))
		
	def sum_versions(self):
		sum = self.version
		for c in self.children:
			sum += c.sum_versions()
		return sum
		
		


def bits_to_int(seq):
	val = 0

	for i in range(len(seq)):
		if seq[-1-i]:
			val += 2**i
		
	return val
			


def hex_to_bits(c):
	list = []
	if c == "0":
		list = [False, False, False, False]
	elif c == "1":
		list = [False, False, False, True]
	elif c == "2":
		list = [False, False, True, False]
	elif c == "3":
		list = [False, False, True, True]
	elif c == "4":
		list = [False, True, False, False]
	elif c == "5":
		list = [False, True, False, True]
	elif c == "6":
		list = [False, True, True, False]
	elif c == "7":
		list = [False, True, True, True]
	elif c == "8":
		list = [True, False, False, False]
	elif c == "9":
		list = [True, False, False, True]
	elif c == "A":
		list = [True, False, True, False]
	elif c == "B":
		list = [True, False, True, True]
	elif c == "C":
		list = [True, True, False, False]
	elif c == "D":
		list = [True, True, False, True]
	elif c == "E":
		list = [True, True, True, False]
	elif c == "F":
		list = [True, True, True, True]	
	
	
	return list


line = ""

# Load file
with  open("input", "r") as f:
	line = f.read().strip()
	

sequence = []
for c in line:
	sequence += hex_to_bits(c)
	

p = Packet(sequence)
print("Sum of all versions is: {}".format(p.sum_versions()))