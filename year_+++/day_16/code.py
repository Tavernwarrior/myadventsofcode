from collections import namedtuple

Operator = namedtuple("Operator", "type sub")


def parse_literal(bin):
    block = slice(bin, 0, 5)
    num = block & 15  # 15 = b01111
    i = 0
    while block & 16:  # 16 = b10000
        i += 1
        block = slice(bin, i*5, (i+1)*5)
        num = (num<<4) + (block & 15)
    return num, (i+1)*5

def parse_op(bin):
    length_bit = slice(bin, 0, 1)
    if length_bit:
        


def parse(binary):
    version = slice(binary, 0, 3)
    type_ = slice(binary, 3, 6)
    if type_ == 4:
        return parse_literal(slice(binary, 6, binary.bit_length()))
    else:
        return parse_op(slice(binary, 6, binary.bit_length()))


def slice(n, x, y):
    return (n >> (n.bit_length() - y)) & (2**(y-x) - 1)


def load_input(path="input.txt"):
    with open(path, "r") as f:
        return int(f.readline(), base=16)