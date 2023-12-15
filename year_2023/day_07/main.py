from collections import Counter
from enum import Enum, IntEnum

INPUT = 'input.txt'


class CardType(IntEnum):
	J = 1
	T = 10
	Q = 12
	K = 13
	A = 14
	
	@staticmethod
	def from_char(char):
		return CardType[char] if not char.isnumeric() else int(char)


class HandType(Enum):
	High = 2
	One_Pair = 4
	Two_Pair = 5
	Three = 6
	Full = 7
	Four = 8
	Five = 10

	@staticmethod
	def from_hand(cards):  # beware changes cards counter
		joker = cards['J']
		cards['J'] = 0  # prevents joker getting counted twice 
		match cards.most_common():
			case [(_, n), (_, 2), *_] if n + joker in (2, 3):
				return HandType((n+joker)*2+1)
			case [(_, n), *_] if n+joker <= 5 and joker > 0:
				return HandType((n+joker)*2) 
			case [(_, n), (_, a), *_] if n in (2, 3) and a+joker == 2:
				return HandType(n*2+1)
			case [(_, n), *_] if n+joker <= 5:
				return HandType((n+joker)*2)
			case [(_, n), *_]:
				return HandType(n*2)
				

if __name__ == '__main__':
	
	camel_game = []
	with open(INPUT, 'r') as file:
		for line in file:
			hand, bet = line.strip().split()
			camel_game.append((tuple(CardType.from_char(c) for c in hand), Counter(hand), int(bet)))
			
	sorted_hands = sorted((HandType.from_hand(cnt).value, hand, bet) for hand, cnt, bet in camel_game)
	
	all_wins = sum((rank+1)*bet for rank, (_, _, bet) in enumerate(sorted_hands))
	print(f'Part One and Two: {all_wins}')
