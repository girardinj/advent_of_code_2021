from generic import get_raw_data, get_raw_data_example

def get_data():
	cleaning_crews = []
	for data in get_raw_data():
		data = data.split(',')
		if len(data) != 2:
			raise Exception(f'data length error! {data}')
		
		d1 = data[0].split('-')
		d2 = data[1].split('-')
		s1 = (int(d1[0]), int(d1[1]))
		s2 = (int(d2[0]), int(d2[1]))

		cleaning_crews.append(Cleaning_Crew(s1, s2))

	return cleaning_crews

class Cleaning_Crew():
	# section is a tuple : (25, 30) means he is cleaning sections [25;30] (both inclusive)
	def __init__(self, section_1, section_2):
		self.section_1 = section_1
		self.section_2 = section_2

	def is_overlaping_exo_1(self):
		start_1 = self.section_1[0]
		end_1 = self.section_1[1]
		start_2 = self.section_2[0]
		end_2 = self.section_2[1]
		
		# if the first section starts after and ends before the second section
		if start_1 >= start_2 and end_1 <= end_2:
			return True
		# if the second section starts after and ends before the first section
		if start_2 >= start_1 and end_2 <= end_1:
			return True
		return False

	def is_overlaping_exo_2(self):
		start_1 = self.section_1[0]
		end_1 = self.section_1[1]
		start_2 = self.section_2[0]
		end_2 = self.section_2[1]
		
		# if the first section starts after the second start, and before the end of the second start
		if start_1 >= start_2 and start_1 <= end_2:
			return True
		# if the second section starts after the first start, and before the end of the first start
		if start_2 >= start_1 and start_2 <= end_1:
			return True
		
		return False
	
	def __str__(self) -> str:
		return f'{self.section_1} - {self.section_2}'

def exo1():
	return len(list(filter(lambda crew: crew.is_overlaping_exo_1(), get_data())))

def exo2():
	return len(list(filter(lambda crew: crew.is_overlaping_exo_2(), get_data())))

def main():
	print(exo1())
	print(exo2())

if __name__ == '__main__':
	main()
