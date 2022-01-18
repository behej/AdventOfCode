
from collections import namedtuple
import copy


Point = namedtuple("Point", ["x", "y", "z"])



class Scanner:
	def __init__(self):
		self.coordinates = Point(0, 0, 0)
		self.points = []
		
		
	def __deepcopy__(self, memo):
		s = Scanner()
		for p in self.points:
			s.add_point(p)
		return s
		
	def __repr__(self):
		return """-- Scanner --
origin: {}
{} points:
- {}""".format(self.coordinates, len(self.points), self.points[0])


	def add_point(self, coord):
		self.points.append(coord)
		
		
	def transform(self, transform_function):
		self.points = [transform_function(p) for p in self.points]
		
	def change_origin(self, new_o):
		self.coordinates = new_o
		
		self.points = [Point(p.x + new_o.x, p.y + new_o.y, p.z + new_o.z) for p in self.points]
		
	def common_points_with(self, scan_ref):
		counter = 0
		for p in self.points:
			if p in scan_ref.points:
				counter += 1
		
		return counter



def transfo1(c):
	"""No transformation
	"""
	return Point(c.x, c.y, c.z)

def transfo2(c):
	"""Rotation aroud x axis, 90° cw
	"""
	return Point(c.x, c.z, -c.y)
	
def transfo3(c):
	"""Rotation aroud x axis, 180° cw
	"""
	return Point(c.x, -c.y, -c.z)
	
def transfo4(c):
	"""Rotation aroud x axis, 90° ccw
	"""
	return Point(c.x, -c.z, c.y)

def transfo5(c):
	"""1st rotation around z 90° ccw
	"""
	return Point(-c.y, c.x, c.z)

def transfo6(c):
	"""1st rotation around z 90° ccw, then rotation around y, 90° cw
	"""
	return Point(-c.z, c.x, -c.y)

def transfo7(c):
	"""1st rotation around z 90° ccw, then rotation around y, 180° cw
	"""
	return Point(c.y, c.x, -c.z)

def transfo8(c):
	"""1st rotation around z 90° ccw, then rotation around y, 90° ccw
	"""
	return Point(c.z, c.x, c.y)

def transfo9(c):
	"""1st rotation around z 180° ccw
	"""
	return Point(-c.x, -c.y, c.z)

def transfo10(c):
	"""1st rotation around z 180° ccw, then rotation around x 90° cw
	"""
	return Point(-c.x, -c.z, -c.y)

def transfo11(c):
	"""1st rotation around z 180° ccw, then rotation around x 180° cw
	"""
	return Point(-c.x, c.y, -c.z)

def transfo12(c):
	"""1st rotation around z 180° ccw, then rotation around x 90° ccw
	"""
	return Point(-c.x, c.z, c.y)

def transfo13(c):
	"""1st rotation around z 90° cw
	"""
	return Point(c.y, -c.x, c.z)

def transfo14(c):
	"""1st rotation around z 90° cw, then rotation around y 90° cw
	"""
	return Point(-c.z, -c.x, c.y)
	
def transfo15(c):
	"""1st rotation around z 90° cw, then rotation around y 180° cw
	"""
	return Point(-c.y, -c.x, -c.z)
	
def transfo16(c):
	"""1st rotation around z 90° cw, then rotation around y 90° ccw
	"""
	return Point(c.z, -c.x, -c.y)

def transfo17(c):
	"""1st rotation around y 90° cw
	"""
	return Point(-c.z, c.y, c.x)

def transfo18(c):
	"""1st rotation around y 90° cw, then rotation around z 90° cw
	"""
	return Point(c.y, c.z, c.x)
	
def transfo19(c):
	"""1st rotation around y 90° cw, then rotation around z 180° cw
	"""
	return Point(c.z, -c.y, c.x)
	
def transfo20(c):
	"""1st rotation around y 90° cw, then rotation around z 90° ccw
	"""
	return Point(-c.y, -c.z, c.x)

def transfo21(c):
	"""1st rotation around y 90° ccw
	"""
	return Point(c.z, c.y, -c.x)

def transfo22(c):
	"""1st rotation around y 90° ccw, then rotation around z 90° cw
	"""
	return Point(c.y, -c.z, -c.x)
	
def transfo23(c):
	"""1st rotation around y 90° ccw, then rotation around z 180° cw
	"""
	return Point(-c.z, -c.y, -c.x)
	
def transfo24(c):
	"""1st rotation around y 90° ccw, then rotation around z 90° ccw
	"""
	return Point(-c.y, c.z, -c.x)


def manhattan_distance(p1, p2):
	return abs(p1.x - p2.x) + abs(p1.y - p2.y) + abs(p1.z - p2.z)


transformations = [transfo1, transfo2, transfo3, transfo4, transfo5, transfo6, \
				   transfo7, transfo8, transfo9, transfo10, transfo11, transfo12, \
				   transfo13, transfo14, transfo15, transfo16, transfo17, transfo18, \
				   transfo19, transfo20, transfo21, transfo22, transfo23, transfo24]


undef_scanners = []

# Load file
with  open("input", "r") as f:
	for l in f:
		if l.strip().startswith("---"):
			s = Scanner()
		elif l.strip() == "":
			undef_scanners.append(s)
		else:
			c = [int(i) for i in l.strip().split(",")]
			c = Point(c[0], c[1], c[2])
			s.add_point(c)
			
	undef_scanners.append(s)
		


scanners = []

# 1st scanner is arbitrarily defined as being at coordinates (0, 0, 0)
scanners.append(undef_scanners.pop(0))

# Now let's try to localize all other scanners in relation to the one already localized
# Principle is:
# - Consider one unlocalized scanner and one localized scanner
# - Make correspond one point of unlocalized scanner to one point of localized scanner
# - Count how many other points are corresponding between both scanners
# - Test all correspondance combinations
# - Test also all possible orientations of unlocalized scanner
# - If 12 points or more are corresponding between both scanner
#	- currently tested orientation and alignment are validated
#	- move scanner to list of localized ones
# Repeat as long as there are remaining unlocalized scanners
while undef_scanners:
	for i in range(len(undef_scanners)):
		found = False

		# Try each transformation
		for t in transformations:
			s2 = copy.deepcopy(undef_scanners[i])
			s2.transform(t)

			# Try to localize currently tested scanner against each already localized scanner
			for scan_ref in scanners:
			
				# Test each point of unlocalized scanner
				for p2 in s2.points:
					
					# Test it against each point of localized scanner
					for p1 in scan_ref.points:
						scan_test = copy.deepcopy(s2)
						p2_abs_pos = Point(p2.x + scan_test.coordinates.x, p2.y + scan_test.coordinates.y, p2.z + scan_test.coordinates.z)
						new_origin = Point(p1.x - p2_abs_pos.x, p1.y - p2_abs_pos.y, p1.z - p2_abs_pos.z)
						scan_test.change_origin(new_origin)

						if scan_test.common_points_with(scan_ref) >= 12:
							print("Correspondance found when aligning {} with {} with transformation{}".format(p2, p1, t))
							scanners.append(scan_test)
							found = True
							break
					
					if found:
						break
					
				if found:
					break
				
			if found:
				break
			
		if found:
			del(undef_scanners[i])
			break
			
	if not found:
		print("Remaining scanners without overlapping area")
		break
	

# Determine largest Manhattan distance
max_dist = 0

for s1 in scanners:
	for s2 in scanners:
		current_dist = manhattan_distance(s1.coordinates, s2.coordinates)
		max_dist = current_dist if current_dist > max_dist else max_dist




print("Largest Manhattan distance between scanners is: {}".format(max_dist))

