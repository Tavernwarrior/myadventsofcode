from calendar import c
import itertools as it
from pprint import pprint

INPUT = "input.txt"


def block_o_num(line):
    border = f'#{line}#'
    return [border.count('O', i, j) for i, j in it.pairwise(i for i, x in enumerate(border) if x=='#')]


def rotate(data):
    return [''.join(dataset[j][-i] for j in range(len(data))) for i in range(len(data[0]))]


if __name__ == '__main__':

    with open(INPUT, 'r') as file:
        dataset = [line.strip() for line in file]

    height = len(dataset)
    width = len(dataset[0])
    dataset_b = ['#'*width]+[f'#{line}#' for line in dataset]+['#'*width]

    dataset_t = [f"#{''.join(dataset[j][i] for j in range(len(dataset)))}#" for i in range(len(dataset[0]))]

    
    curr = None

    hash_pos = [[i for i, x in enumerate(line) if x=='#'] for line in curr]

    num_o_s = [[line.count('O', j, k) for j, k in it.pairwise(hash_pos[i])] for i, line in enumerate(curr)]

    
    print(sum(sum(sum(range(height-k, height-(k+cnt), -1)) for cnt, k in zip(no, hp)) for no, hp in zip(num_o_s, hash_pos)))
    #print(num_o_s)
    #print(block_o_num('O.#..O.#.#'))
