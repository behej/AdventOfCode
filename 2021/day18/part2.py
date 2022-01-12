
class Sailfish:
	def __init__(self, s, d=0):
		self.left = 0
		self.right = 0
		self.depth = d
		
		if s[0] != "[":
			return
		del(s[0])
		
		if s[0] == "[":
			self.left = Sailfish(s, self.depth+1)
		elif s[0].isdigit():
			self.left = int("".join(s[:s.index(",")]))	
		del(s[:s.index(",")+1])
		
		if s[0] == "[":
			self.right = Sailfish(s, self.depth+1)
		elif s[0].isdigit():
			self.right = int("".join(s[:s.index("]")]))
		del(s[:s.index("]")+1])
		
		
	
	def __repr__(self):
		return("[{},{}]".format(self.left, self.right))
		
	def __add__(self, b):
		s =  Sailfish(list("[{},{}]".format(self, b)))
		s.reduce()
		return s
		
	def reduce(self):
		while self.max_depth() >= 4 or self.needs_split():
			self.explode()
			self.split()
			
	def magnitude(self):
		"""Magnitude is 3x left magnitude + 2x right magnitude
		"""
		
		l_mag = (self.left if type(self.left) == int else self.left.magnitude())
		r_mag = (self.right if type(self.right) == int else self.right.magnitude())
		return 3*l_mag + 2*r_mag
			
			
	def explode(self):
		while self.max_depth() >= 4:
			self.__explode__()
			
	def __explode__(self):
		"""Explode element itself or child elements.
		
		Returns None if no child elements have exploded.
		Returns a tuple if exploded. Tuple may contain values to propagate to neighbors.
		"""
	
			
		# Start with left
		#================
		# Left is final and depth level higher than 4 -> it explodes directly
		if type(self.left) != int and self.left.is_final() and self.left.depth >= 4:
			l, r = self.left.left, self.left.right
			self.left = 0
			if type(self.right) == int:
				self.right += r
			else:
				self.right.add_to_left(r)
			return (l, 0)
		
		# Left is not final, so let ask it to explode
		if type(self.left) != int and not self.left.is_final():
			ex = self.left.__explode__()
			
			# left exploded:
			# - right value of tuple needs to be added to right part
			# - left value of tuple needs to be passed to parent item
			if ex:
				l,r = ex
				if type(self.right) == int:
					self.right += r
				else:
					self.right.add_to_left(r)
				return (l,0)
				
		# Left didn't explode (neither any of its children) -> consider right part
		#=====================================================================
		# Right is final and depth >= 4 -> it explodes directly
		if type(self.right) != int and self.right.is_final() and self.right.depth >= 4:
			l,r = (self.right.left, self.right.right)
			self.right = 0
			if type(self.left) == int:
				self.left += l
			else:
				self.left.add_to_right(l)
			return (0,r)
			
		# Right is not final, let ask it to explode
		if type(self.right) != int and not self.right.is_final():
			ex = self.right.__explode__()
			
			# Right exploded:
			# - left value of tuple is added to left
			if ex:
				(l,r) = ex
				if type(self.left) == int:
					self.left += l
				else:
					self.left.add_to_right(l)
				return (0,r)
		
		# If reaching here, nobody exploded
		return None
		
	def split(self):
		if type(self.left) == int and self.left > 9:
			self.left = Sailfish(list("[{},{}]".format(self.left//2, self.left - self.left//2)), self.depth+1)
			return True
			
		if type(self.left) != int:
			if self.left.split():
				return True
			
		if type(self.right) == int and self.right > 9:
			self.right = Sailfish(list("[{},{}]".format(self.right//2, self.right - self.right//2)), self.depth+1)
			return True
		if type(self.right) != int:
			if self.right.split():
				return True
				
		return False
		
	def max_depth(self):
		l_depth = self.depth if type(self.left) == int else self.left.max_depth()
		r_depth = self.depth if type(self.right) == int else self.right.max_depth()
		return max(l_depth, r_depth)
			
	def is_final(self):
		return type(self.left) == int and type(self.right) == int
		
	def needs_split(self):
		return (type(self.left) == int and self.left > 9) \
			or (type(self.left) != int and self.left.needs_split()) \
			or (type(self.right) == int and self.right > 9) \
			or (type(self.right) != int and self.right.needs_split())
		
		
	def add_to_left(self, val):
		if type(self.left) == int:
			self.left += val
		else:
			self.left.add_to_left(val)

	def add_to_right(self, val):
		if type(self.right) == int:
			self.right += val
		else:
			self.right.add_to_right(val)
		


numbers = []
max_mag = 0

# Load file
with  open("input", "r") as f:
	for line in f:
		numbers.append(Sailfish(list(line.strip())))
		
		
for s1 in numbers:
	for s2 in numbers:
		sum = s1 + s2
		mag = sum.magnitude()
		max_mag = mag if mag > max_mag else max_mag
		
		
		
print("Maximum magnitude is: {}".format(max_mag))

