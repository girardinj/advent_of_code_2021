from generic import get_raw_data, get_raw_data_example

from enum import Enum

class Choice(Enum):
	Rock = 1
	Paper = 2
	Scissors = 3

	def lose_against(self):
		if self == Choice.Rock:
			return Choice.Paper
		elif self == Choice.Paper:
			return Choice.Scissors
		elif self == Choice.Scissors:
			return Choice.Rock
		else:
			return None
	
	def win_against(self):
		if self == Choice.Rock:
			return Choice.Scissors
		elif self == Choice.Paper:
			return Choice.Rock
		elif self == Choice.Scissors:
			return Choice.Paper
		else:
			return None

	


class Strat():
	def __init__(self, opponent, you, exo_num):
		
		# A : Rock
		# B : Paper
		# C : Scissors
		# exo 1:
		# X : Rock
		# Y : Paper
		# Z : Scissors
		# exo 2:
		# X : I need to lose
		# Y : I need to tie
		# Z : I need to win
		if (opponent == 'A'):
			self.opponent = Choice.Rock
		elif (opponent == 'B'):
			self.opponent = Choice.Paper
		elif (opponent == 'C'):
			self.opponent = Choice.Scissors
		else:
			raise Exception(f'opponent is playing an unknown value [{opponent}]')

		if exo_num == 1:
			if (you == 'X'):
				self.you = Choice.Rock
			elif (you == 'Y'):
				self.you = Choice.Paper
			elif (you == 'Z'):
				self.you = Choice.Scissors
			else:
				raise Exception(f'you are playing an unknown value [{you}]')

		elif exo_num == 2:
			if (you == 'X'):
				self.you = self.opponent.win_against()
			elif (you == 'Y'):
				self.you = self.opponent
			elif (you == 'Z'):
				self.you = self.opponent.lose_against()
			else:
				raise Exception(f'wtf ?! [{you}]')
		
		else:
			raise Exception(f'there can be only two exo numbers ! [{exo_num}]')

	def get_score(self):
		total = self.you.value
		
		if (self.opponent == Choice.Rock):
			if (self.you == Choice.Rock):
				total += 3
			elif (self.you == Choice.Paper):
				total += 6
		elif (self.opponent == Choice.Paper):
			if (self.you == Choice.Paper):
				total += 3
			elif (self.you == Choice.Scissors):
				total += 6
		elif (self.opponent == Choice.Scissors):
			if (self.you == Choice.Scissors):
				total += 3
			elif (self.you == Choice.Rock):
				total += 6
				
		return total

def get_data():
	data = []
	for line in get_raw_data():
		l = line.split()
		if len(l) != 2:
			raise Exception('wtf')
		data.append((l[0], l[1]))
	return data

def exo1():
	strats = []
	for data in get_data():
		strats.append(Strat(data[0], data[1], 1))
		
	return sum(strat.get_score() for strat in strats)

def exo2():
	strats = []
	for data in get_data():
		strats.append(Strat(data[0], data[1], 2))
		
	return sum(strat.get_score() for strat in strats)

def main():
	print(exo1())
	print(exo2())

if __name__ == '__main__':
	main()
