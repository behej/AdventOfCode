import pandas as pd


def flash(x, y):
	"""Flash octopus at given coordinates and transfer energy to neighbors.
	
	Reset energy level to 0. Flash is received by each of 8 neighbors (pay attention
	to octopuses at grid edges).
	"""
	global A
	
	# Reset energy level
	A.iloc[y,x] = 0
	
	# Increase energy level of neighbors
	#===================================
	# Top left
	if (x > 0) and (y > 0):
		receive_flash(x-1, y-1)
	# Top
	if (y > 0):
		receive_flash(x, y-1)
	# Top right
	if (x < A.shape[1]-1) and (y > 0):
		receive_flash(x+1, y-1)
	# Left
	if (x > 0):
		receive_flash(x-1, y)
	# Right
	if (x < A.shape[1]-1):
		receive_flash(x+1, y)
	# Bottom left
	if (x > 0) and (y < A.shape[0]-1):
		receive_flash(x-1, y+1)
	# Bottom
	if (y< A.shape[0]-1):
		receive_flash(x, y+1)
	# Bottom right
	if (x < A.shape[1]-1) and (y < A.shape[0]-1):
		receive_flash(x+1, y+1)
	
	
def receive_flash(x, y):
	"""Receive flash from another octopus.
	
	Increase energy level by 1. If energy level reaches 10 or above, flash and
	propagate flash to adjacent octopuses.
	"""
	global A
	
	# Do not increase energy level is already to 0 (that means it just flashed and shouldn't reflash)
	if A.iloc[y, x] > 0:
		A.iloc[y, x] += 1
		
	# If energy level reaches 9, it flashes immediately
	if A.iloc[y, x] > 9:
		flash(x, y)


def count_flashes():
	"""Count how many octopuses just flashed.
	
	Octopus just flashed if energy level is 0. Count how many
	cells are equals to 0.
	"""
	global A
	
	counter = 0
	for y in range(A.shape[0]):
		for x in range(A.shape[1]):
			counter += 1 if (A.iloc[y,x] == 0) else 0

	return counter

width = 0

with  open("input", "r") as f:
	l = f.readline().strip()
	width = len(l)

A = pd.read_fwf("input", header=None, widths=[1]*width)


round = 0
synchro = False

while not synchro:
	round += 1
	A += 1
	
	print("Round {}".format(round))
	for y in range(A.shape[0]):
		for x in range(A.shape[1]):
			if A.iloc[y,x] > 9:
				flash(x, y)
			
	# All octopuses flashed
	if count_flashes() == A.shape[0] * A.shape[1]:
		synchro = True
	
	
print("All octopuses flashed synchronously at round {}".format(round))	
	


