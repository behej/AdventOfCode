
def winners(scores):
	return [count for count,score in enumerate(scores) if score >= 1000]

def augment_dice(dice):
	return (dice + 1) if dice < 100 else 1
	
def move_player(start_pos, count):
	pos = start_pos + count
	return ((pos - 1) % 10) + 1
	

players = []



# Load file
with  open("input", "r") as f:
	for l in f:
		players.append(int(l.strip().split()[-1]))
		
scores = [0 for p in players]



round = 0
dice = 1


while not winners(scores):
	current_player = round % len(players)
	round += 1
	
	dice_result = 0
	for i in range(3):
		dice_result += dice
		dice = augment_dice(dice)
		
	players[current_player] = move_player(players[current_player], dice_result)
	scores[current_player] += players[current_player]
	
	
loser = 1 - winners(scores)[0]
loser_score = scores[loser]

dice_rolled = round * 3

print("Loser has {} points".format(loser_score))
print("Dice has been rolled {} times".format(dice_rolled))
print("Result is: {}".format(loser_score * dice_rolled))