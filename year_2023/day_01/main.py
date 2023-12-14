import re
INPUT = 'input.txt'


if __name__ == '__main__':
	
	nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	
	first_reg = re.compile(r'(\d)|' + "|".join(f"({n})" for n in nums))
	last_reg = re.compile(r'(\d)|' + "|".join(f"({n[::-1]})" for n in nums))
	
	def convert(n):
		return int(n) if n.isnumeric() else nums.index(n)+1

	def find_first_last(line):
		first = first_reg.search(line)
		last = last_reg.search(line[::-1])
		return convert(first.group()), convert(last.group()[::-1])

	with open(INPUT, 'r') as file:
		read_nums = [find_first_last(line) for line in file]
	
	result = sum(f*10+l for f, l in read_nums)
	print(f'Part Two: {result}')
			
			