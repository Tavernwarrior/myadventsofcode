import pprint


INPUT = 'input.txt'

def debug_print(func):
    def inner(seq, blocks):
        #print('##', seq, blocks)
        res = func(seq, blocks)
        #print(seq, blocks, res)
        return res
    return inner

import functools

@functools.lru_cache(maxsize=1024)
def nums(seq, blocks):

    y = seq.find('?')+1 or len(seq)
    xx = seq.find('#')
    x = xx+1 or len(seq)
    if len(blocks) == 0:
        return int(xx == -1)

    seq = seq[max(min(x, y)-1, 0):]

    i = seq.find('.')
    if i == -1:
        i = len(seq)
    j = seq[:i].find('#')
    
    b = blocks[0]
    if b == len(seq) and len(blocks)==1:
        return int('.' not in seq)
    elif b>=len(seq):
        return 0

    if j == -1:
        if b > i:
            return nums(seq[i:], blocks) # no block possible
        else:
            return sum(nums(seq[k+b+1:], blocks[1:]) for k in range(i-b+1)) + nums(seq[i:], blocks)  # no # possible
    else:
        accum = sum(nums(seq[k+b+1:], blocks[1:]) for k in range(max(j-b, 0)))  # set block befor #, can be zero
        accum += sum(nums(seq[k+b+1:], blocks[1:]) for k in range(max(j-b, 0), min(i+1-b, j+1)) if k+b>= len(seq) or seq[k+b] != '#') # set block with #
        return accum
    

if __name__ == '__main__':
    with open(INPUT, 'r') as file:
        dataset = [((n:=line.split())[0],[int(num) for num in n[1].split(',')]) for line in file]

    ext_dataset = [(f'{seq}?{seq}?{seq}?{seq}?{seq}', tuple(block*5)) for seq, block in dataset]

    print('Part One:', sum(nums(seq, block) for seq, block in dataset))
    print('Part Two:', sum(nums(seq, block) for seq, block in ext_dataset))
