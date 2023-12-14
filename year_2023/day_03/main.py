
INPUT = 'input'


if  __name__ == "__main__":
	symbols = []
	numbers = []
	with open(INPUT, 'r') as f:
		for j, line in enumerate(f.readlines()):
			i = 0
			row_numbers = []
			while (c := line[i]) != '\n':
				if c == '.':
					i += 1
				elif c.isnumeric():
					end = i+1
					while (nc := line[end]).isnumeric():
						end += 1
					row_numbers.append((j, i, end, int(line[i:end])))
					i = end
				else:
					symbols.append((j, i, c))
					i += 1
			numbers.append(row_numbers)
	
	# Part One
	part_numbers = []
	for j, i, sym in symbols:
		for y in range(j-1, j+2):
			for _, start, end, number in numbers[y]:
				if start > i+1:
					break
				elif i in range(start-1, end+1):
					part_numbers.append(number)
	
	# Part Two
	possible_gears = ((y, x) for y, x, sym in symbols if sym == '*')
	gears = []
	for j, i in possible_gears:
		found_numbers = []
		for y in range(j-1, j+2):
			for _, start, end, number in numbers[y]:
				if start > i+1:
					break
				elif i in range(start-1, end+1):
					found_numbers.append(number)
		if len(found_numbers) == 2:
			gears.append((j, i, *found_numbers))
	
	# print(part_numbers)
	print(f'Part One: {sum(part_numbers)}')
	print(f'Part Two: {sum(a*b for _, _, a, b in gears)}')
