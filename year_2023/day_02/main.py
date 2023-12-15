import re
INPUT = 'input.txt'


if __name__ == '__main__':
	games = []
	with open(INPUT, 'r') as file:
		for line in file:
			game_id = int(re.match(r"Game (\d+): ([\w ,;]+)", line).group(1))
			game_res = (re.findall(r"(\d+) (\w+)", result) for result in m.group(2).split(';'))
			res_dict = [{color: int(num) for num, color in res} for res in game_res]
			games.append((game_id, res_dict))
		
	# Part Two
	
	accum = 0
	for _, res in games:
		red = max(map.get('red', 0) for map in res)
		green = max(map.get('green', 0) for map in res)
		blue = max(map.get('blue', 0) for map in res)
		accum += red*green*blue
		
	print(f'Part Two: {accum}')
