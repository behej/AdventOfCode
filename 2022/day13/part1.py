#! /usr/bin/python3


class Number:
	def __init__(self, s):
		print('CTor')
		print(s)
		self.__list = []
		if s[0] != '[':
			return
		del(s[0])
		print(s)

		while s[0] != ']':
			if s[0].isdigit():
				number = ''
				while s[0].isdigit():
					number += s[0]
					del(s[0])
				self.__list.append(int(number))
				print(self.__list)
			elif s[0] == '[':
				self.__list.append(Number(s))

			if s[0] == ',':
				del(s[0])
		print('last char {}'.format(s[0]))
		del(s[0])
		print('-> {}'.format(s))


	def __str__(self):
		l = []
		for i in self.__list:
			if isinstance(i, int):
				l.append(str(i))
			else:
				l.append(i.__str__())
		return '[' + ','.join(l) + ']'

	def __eq__(self, other):
		if isinstance(other, int):
			other = Number(list('[{}]'.format(other)))
			print('other is int')
			# return True

		if len(self.__list) != len(other.__list):
			print('different length')
			return False
		for val1, val2 in zip(self.__list, other.__list):
			if val1 != val2:
				return False

		return True


	def __lt__(self, other):
		if isinstance(other, int):
			other = Number(list('[{}]'.format(other)))

		for i in range(min(len(self.__list), len(other.__list))):
			val1 = self.__list[i]
			val2 = other.__list[i]
			#if type(val1) == type(val2):
			if val1 != val2:
				return val1 < val2
			# else:
			# 	print('types diff')
			# 	return True
		return len(self.__list) < len(other.__list)

	def __gt__(self, other):
		if isinstance(other, int):
			other = Number(list('[{}]'.format(other)))

		for i in range(min(len(self.__list), len(other.__list))):
			val1 = self.__list[i]
			val2 = other.__list[i]
			#if type(val1) == type(val2):
			if val1 != val2:
				return val1 > val2
			# else:
			# 	print('types diff')
			# 	return True
		return len(self.__list) > len(other.__list)


total = 0

pairs = open('input', 'r').read().split('\n\n')
for i, p in enumerate(pairs):
	p1 = Number(list(p.split()[0]))
	p2 = Number(list(p.split()[1]))
	if p1 < p2:
		total += (i+1)


print(total)
