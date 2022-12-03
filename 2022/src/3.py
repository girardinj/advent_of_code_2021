from generic import get_raw_data, get_raw_data_example

class Rucksack_exo1():
	def __init__(self, content):
		if len(content) % 2 != 0:
			raise Exception('odd number of content')
		
		half = int(len(content)/2)
		self.left_side = content[:half]
		self.right_side = content[half:]

		''' we do not care if the item is there multiple times, it only need to be seen once to be as "shared"
		self.shared_content = []
		indexes = []
		for i in range(len(self.left_side)):
			cl = self.left_side[i]
			for j in range(len(self.right_side)):
				cr = self.right_side[j]
				if cl == cr:
					indexes.append(i)
					self.right_side = self.right_side[:j] + self.right_side[j+1:]
					self.shared_content.append(cl)
					break
		indexes.reverse()
		for i in indexes:
			self.left_side = self.left_side[:i] + self.left_side[i+1:]
		'''
		
		self.shared_content = set(shared for shared in self.left_side if shared in self.right_side)

	def shared_content_value(self):
		# a-z => 1-26
		# A-Z => 27-52
		total = 0

		for c in self.shared_content:
			if ord(c) >= ord('a') and ord(c) <= ord('z'):
				total += ord(c) - ord('z') + 26
				#print(c, total)
			
			elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
				total += ord(c) - ord('Z') + 52
				#print(c, total)

		return total

	def __str__(self) -> str:
		return f'left side: {self.left_side}\nright side: {self.right_side}\nshared: {self.shared_content}'

class Rucksack_exo2():
	def __init__(self, content1, content2, content3):
		shared = set()
		for c in content1:
			if c in content2 and c in content3:
				shared.add(c)

		self.shared_content = []
		for c in shared:
			self.shared_content.append((c, min(content1.count(c), content2.count(c), content3.count(c))))

	def shared_content_value(self):
		# a-z => 1-26
		# A-Z => 27-52
		total = 0

		for c, count in self.shared_content:
			#print(c, count)
			if ord(c) >= ord('a') and ord(c) <= ord('z'):
				total += ord(c) - ord('z') + 26
				#print(c, total)
			
			elif ord(c) >= ord('A') and ord(c) <= ord('Z'):
				total += ord(c) - ord('Z') + 52
				#print(c, total)

		return total

	def __str__(self) -> str:
		return f'left side: {self.left_side}\nright side: {self.right_side}\nshared: {self.shared_content}'


def get_data_1():
	data = []
	for line in get_raw_data():
		data.append(Rucksack_exo1(line))
	return data
	

def get_data_2():
	data = []
	raw_data = get_raw_data()
	i = 0
	while i + 2 < len(raw_data):
		data.append(Rucksack_exo2(raw_data[i], raw_data[i+1], raw_data[i+2]))
		i += 3
	return data

def exo1():
	data = get_data_1()
	return sum(backpack.shared_content_value() for backpack in data)

def exo2():
	return sum(d.shared_content_value() for d in get_data_2())

def main():
	print(exo1())
	print(exo2())

if __name__ == '__main__':
	main()
