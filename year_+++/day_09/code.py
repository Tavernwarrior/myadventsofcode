from itertools import chain
import sys

sys.setrecursionlimit(10000)

def load_input():
    with open("input.txt", "r") as f:
        data = [[int(c) for c in n.strip()] for n in f.readlines()]
    return data


def check(mat, mask, off_x, off_y):
    width = len(mat)
    height = len(mat[0])

    for x in range(max(-off_x, 0), min(width - off_x, width)):
        for y in range(max(-off_y, 0), min(height - off_y, height)):
            mask[x][y] &= mat[x][y] < mat[x + off_x][y + off_y]


def rec_basin(mat, map, x, y, width, height):
    if x not in range(0, width) or y not in range(0, height):
        return
    map[x][y] = True
    pos = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for xd, yd in pos: 
        x0 = x + xd
        y0 = y + yd
        if mat[x0][y0] != 9:
            rec_basin(mat, map, x0, y0, width, height)


def biggest_basins(mat, low, width, height):
    basins_sizes = []
    for x in range(width):
        for y in range(height):
            if low[x][y]:
                basin = [[False for _ in mat[0]] for _ in mat]
                rec_basin(mat, basin, x, y, width, height)
                basins_sizes.append(sum(int(v) for v in chain.from_iterable(basin)))

    return sorted(basins_sizes)

def height(mat):
    width = len(mat)
    height = len(mat[0])
    low = [[True for _ in mat[0]] for _ in mat]

    check(mat, low, 1, 0)
    check(mat, low, -1, 0)
    check(mat, low, 0, 1)
    check(mat, low, 0, -1)

    result = 0

    for x in range(width):
        for y in range(height):
            if low[x][y]:
                result += mat[x][y] + 1

    return biggest_basins(mat, low, width, height)
