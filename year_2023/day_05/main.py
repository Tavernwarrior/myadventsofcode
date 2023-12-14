INPUT = 'input'


if __name__ == '__main__':
	
	with open(INPUT, 'r') as file:
		seeds = [int(id) for id in file.readline()[6:-1].split()]
		file.readline()
		
		maps = []
		
		for _ in range(7):
			file.readline()
			map_ = []
			while (line := file.readline().rstrip('\n')) != '':
				map_.append(tuple(int(n) for n in line.split()))
			maps.append(map_)
		
		
	# Part One
	def map_value(val, map):
		for dest, source, step in map:
			if source <= val < source+step:
				return dest + (val - source)
		return val
	
	def map_values(vals, map):
		return [map_value(val, map) for val in vals]
	
	mapped = seeds
	for map in maps:
		mapped = map_values(mapped, map)
	
	print(f'Part One:', min(mapped))
	
	# Part Two
	
	def _map_range(ran, map):
		dest, source, map_step = map
		start, ran_step = ran
		end = start+ran_step
		if start > source+map_step or start+ran_step < source:
			return [ran], []
		over_end = min(end, source+map_step)
		over_start = max(start, source)
		res = [(start, over_start-start), (over_end, end-over_end)]
		return [r for r in res if r[1] > 0], [(dest+(over_start-source), over_end-over_start)] if over_end-over_start > 0 else []
		
	def map_range(ran, map):
		rans = ran
		res = []
		for m in map:
			new_ran = []
			for r in rans:
				a, b = _map_range(r, m)
				new_ran += a
				res += b
			rans = new_ran
		return rans + res
	
	results = []
	for seed_range in zip(seeds[::2], seeds[1::2]):
		vals = seed_range
		mapped = [vals]
		for map in maps:
			mapped = map_range(mapped, map)
			
		results += mapped

	print(f'Part Two:', min(results, key=lambda x: x[0])[0])