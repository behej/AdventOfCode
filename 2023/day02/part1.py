#!/usr/bin/python3



limits = {'red': 12, 'green': 13, 'blue': 14}

sum = 0

games = {}
with open("input.txt", "r") as f:
    for l in f:
        game_id = int(l.split(':')[0].split(' ')[-1])
        games[game_id] = []
        possible = True

        l = l.split(':')[1].strip()

        for set in l.split(';'):
            colors = {}
            
            for rev in set.split(','):
                c = rev.strip().split(' ')[1]
                q = int(rev.strip().split(' ')[0])
                colors[c] = q

                if q > limits[c]:
                    possible = False
                    break
            
            games[game_id].append(colors)



        if possible:
            sum += game_id
            
print(sum)