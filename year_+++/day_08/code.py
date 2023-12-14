import sys 
from itertools import chain


def load_input():
    with open("input.txt", "r") as f:
        data = [((s := n.split(" | "))[0].split(), s[1].split()) for n in f.readlines()]
    return data

def count(ar):
    out = list(zip(*ar))
    return sum( int(len(d) in {2, 4, 3, 7})  for d in chain.from_iterable(out[1]))