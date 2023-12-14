import re

INPUT = 'input'


if __name__ == '__main__':
	cards = []
	
	card_regex = re.compile(r"Card +([\d]+): ([\d ]+)\| ([\d ]+)")
	with open(INPUT, 'r') as file:
		for line in file.readlines():
			res = card_regex.match(line)
			game_num = res.group(1)
			win_nums = {int(n) for n in res.group(2).split()}
			picked_nums = [int(n) for n in res.group(3).split()]
			cards.append((game_num, win_nums, picked_nums))
		
	# Part One
	won = [sum(pick in win for pick in picked) for _, win, picked in cards]
	
	accum = sum(2**(win-1) for win in won if win != 0)
	print('Part One: ', accum)

	# Part Two
	
	copies = [1]*len(cards)

	for i, won in enumerate(won):
		for j in range(i, min(i+won, len(cards))):
			copies[j+1] += copies[i]
	
	print('Part Two: ', sum(copies))