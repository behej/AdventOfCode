

def move_player(start_pos, count):
	pos = start_pos + count
	return ((pos - 1) % 10) + 1
	
	
	
def new_dice(pos1, pos2, score1, score2, dice_val, freq, round):
	global wins1
	global wins2
	global comb
	
	player = round % 2

	if player == 0:
		pos1 = move_player(pos1, dice_val)
		score1 += pos1
		if (score1 >= 21):
			wins1 += freq
		else:
			for (dice, f) in comb.items():
				new_dice(pos1, pos2, score1, score2, dice, freq*f, round+1)			
	
	else:
		pos2 = move_player(pos2, dice_val)
		score2 += pos2
		if (score2 >= 21):
			wins2 += freq
		else:
			for (dice, f) in comb.items():
				new_dice(pos1, pos2, score1, score2, dice, freq*f, round+1)




# 1, 1, 1 = 3
# 1, 1, 2 = 4
# 1, 1, 3 = 5
# 1, 2, 1 = 4
# 1, 2, 2 = 5
# 1, 2, 3 = 6
# 1, 3, 1 = 5
# 1, 3, 2 = 6
# 1, 3, 3 = 7
# 2, 1, 1 = 4
# 2, 1, 2 = 5
# 2, 1, 3 = 6
# 2, 2, 1 = 5
# 2, 2, 2 = 6
# 2, 2, 3 = 7
# 2, 3, 1 = 6
# 2, 3, 2 = 7
# 2, 3, 3 = 8
# 3, 1, 1 = 5
# 3, 1, 2 = 6
# 3, 1, 3 = 7
# 3, 2, 1 = 6
# 3, 2, 2 = 7
# 3, 2, 3 = 8
# 3, 3, 1 = 7
# 3, 3, 2 = 8
# 3, 3, 3 = 9
# score = 3 -> 1 combination
# score = 4 -> 3 combinations
# score = 5 -> 6 combinations
# score = 6 -> 7 combinations
# score = 7 -> 6 combinations
# score = 8 -> 3 combinations
# score = 9 -> 1 combination

comb = {3: 1, 4:3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


# Load file
with  open("input", "r") as f:
	pos1 = int(f.readline().strip().split()[-1])
	pos2 = int(f.readline().strip().split()[-1])
		
		
score1 = score2 = 0
wins1 = wins2 = 0

round = 0



for (dice_val, freq) in comb.items():
	new_dice(pos1, pos2, score1, score2, dice_val, freq, 0)
	
	


print("Solution is {}".format(max(wins1, wins2)))
