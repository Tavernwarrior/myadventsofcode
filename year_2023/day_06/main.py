import re
import math

INPUT = 'input.txt'
NUM_REG = re.compile(r'(\d+)')

if __name__ == '__main__':

	with open(INPUT, 'r') as file:
		raw_times = NUM_REG.findall(file.readline())
		raw_points = NUM_REG.findall(file.readline())
		times = (int(time) for time in raw_times)
		points = (int(point) for point in raw_points)
		data = list(zip(times, points))
		data.append((int(''.join(raw_times)), int(''.join(raw_points))))
	
	def pq_math(p, q):
		return p/2 - (p**2/4 - q)**0.5
	
	poss = [t - 2*int(pq_math(t, p)) -1 for t, p in data]
	
	print(f'Part One: {math.prod(poss[:-2])}')
	print(f'Part Two: {poss[-1]}')
