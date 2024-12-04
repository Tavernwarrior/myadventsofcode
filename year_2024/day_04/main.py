import re
from pprint import pp


if __name__ == '__main__':

    with open('input') as f:
        data = [line.strip() for line in f.readlines()]


    def get_neighbours(x, y, height, width):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0) and 0 <= x+i < width and 0 <= y+j < height:
                    yield x+i, y+j

    def isin(x, y, height, width):
        return 0 <= x < width and 0 <= y < height

    def recrec(x, y, grid, depth, word='XMAS'):
        nsum = 0
        for nx, ny in get_neighbours(x, y, len(grid), len(grid[0])):
            nsum += rec(nx, ny, nx-x, ny-y, grid, depth+1)

        return nsum

    def rec(x, y, dx, dy, grid, depth, word='XMAS'):
        if depth == len(word)-1 and isin(x, y, len(grid), len(grid[0])) and grid[y][x] == word[-1]:
            return 1
        elif not isin(x, y, len(grid), len(grid[0])) or grid[y][x] != word[depth]:
            return 0
        else:
            return rec(x+dx, y+dy, dx, dy, grid, depth+1, word)

    # Part I
    print(sum(recrec(x, y, data, 0) for y, line in enumerate(data) for x, c in enumerate(line) if c == 'X'))


    def isxmas(x, y, grid):
        if x == 0 or x == len(grid[0])-1 or y == 0 or y == len(grid)-1:
            return 0
        else:
            if (ul := grid[y+1][x+1]) != (dl:=grid[y-1][x-1]) and ul in ('S', 'M') and dl in ('S', 'M'):
                if (ur := grid[y-1][x+1]) != (dr:=grid[y+1][x-1]) and ur in ('S', 'M') and dr in ('S', 'M'):
                    return 1
            return 0

    # Part II
    print(sum(isxmas(x, y, data) for y, line in enumerate(data) for x, c in enumerate(line) if c == 'A'))