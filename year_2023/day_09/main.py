INPUT = 'input.txt'


if __name__ == '__main__':

	with open(INPUT, 'r') as file:
		dataset = [[int(v) for v in line[:-1].split()] for line in file]

	res_r = []
	res_l = []
	for data in dataset:
		d = [data]
		while any(last := d[-1]):
			d.append([r-l for l, r in zip(last[:-1], last[1:])])
		
		res_r.append(sum(next_[-1] for next_ in d[:-1]))
		res_l.append(sum((-1)**i * next_[0] for i, next_ in enumerate(d[:-1])))

	print(f'Part One:{sum(res_r)}')
	print(f'Part Two:{sum(res_l)}')
