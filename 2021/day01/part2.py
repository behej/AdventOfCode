


from collections import deque



deq = deque(maxlen = 3)
deq.append(9999)
deq.append(9999)
deq.append(9999)
counter = 0
prev = 99999

with open("input", "r") as f:
	for line in f:
		deq.append(int(line))
			
		if (sum(deq) > prev):
			counter += 1
		prev = sum(deq)
		
print(counter)
	