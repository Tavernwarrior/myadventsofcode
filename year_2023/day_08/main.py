import re
import math

INPUT = 'input.txt'
NODE_RE = re.compile(r'(\w+) = \((\w+), (\w+)\)')

if __name__ == '__main__':
	
	with open(INPUT, 'r') as file:
		instructions = file.readline().rstrip()
		file.readline()
		data = (NODE_RE.match(line).groups() for line in file)
		map = {src: (destl, destr) for src, destl, destr in data}
	
	def find_end(start):
		current = start
		steps = 0
		while True:
			if current[-1] == 'Z':
				return current, steps
			instruction = instructions[steps%len(instructions)]
			current = map[current][0 if instruction == 'L' else 1]
			steps += 1

	print(f'Part One: {find_end("AAA")}')

	circles = [find_end(src) for src in map if src[-1] == 'A']
	common_circle = math.lcm(*[steps for _, steps in circles])

	print(f'Part Two: {common_circle}')
