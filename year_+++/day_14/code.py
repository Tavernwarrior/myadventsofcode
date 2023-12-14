from itertools import pairwise


def polymerization(symbols, rules, steps):
    if steps == 0:
        return symbols

    res = ""
    for p0, p1 in pairwise(symbols):
        res += polymerization(p0 + rules.get(p0+p1, "") + p1, rules, steps - 1)[:-1]
    return res

def load_input(path="input.txt"):
    with open(path, "r") as f:
        syms = f.readline().strip()
        f.readline()
        rules = dict({tuple(line.strip().split(" -> ")) for line in f})
    return syms, rules
