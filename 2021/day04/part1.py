
numbers = []
grids = []
gridsize = 5





	
class Grid:
	def __init__(self, lines):
		self.lines = list(lines)
		self.cols = []
		
		for i in range(len(lines[0])):		
 			self.cols.append([l[i] for l in lines])
			
		
	def __str__(self):
		return "Lines: {}\nColumns: {}".format(self.lines, self.cols)

		
	def play(self, number):
		for l in self.lines:
			if (number in l):
				l.remove(number)
		for c in self.cols:
			if number in c:
				c.remove(number)
			
	def isWinning(self):
		return (self.isLineWinning() or self.isColWinning())
		
	def isLineWinning(self):
		result = False
		for l in self.lines:
			if sum(l) == 0:
				result = True
		return result
				
	def isColWinning(self):
		result = False
		for c in self.cols:
			if sum(c) == 0:
				result = True
		return result
		
	def score(self):
		return sum([sum(l) for l in self.lines])
	
	
		
		

		
		

with open("input", "r") as f:
	# Get random numbers
	numbers = f.readline().strip().split(",")
	numbers = [int(i) for i in numbers]
	
	# Read grids
	for skipBlankLines in f:
		lines = []
		for i in range(gridsize):
			line = f.readline().strip().split()
			line = [int(i) for i in line]
			lines.append(line)
			
		grids.append(Grid(lines))
		
	
# Start playing

score = 0
lastNumber = 0

for n in numbers:
	for (i,g) in zip(range(len(grids)) , grids):
		g.play(number=n)
		
		if g.isWinning():
			print("Winning grid: {}".format(i))
			print("Last number: {}".format(n))
			score = g.score()
			break
	
	if (score != 0):
		lastNumber = n
		break

print("Score: {}".format(score))
print("Last number: {}".format(lastNumber))
print("Result: {}".format(score*lastNumber))		