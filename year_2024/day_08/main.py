import itertools as it
from collections import defaultdict


if __name__ == '__main__':

    with open('input') as f:
        data_grid = [[t for t in line.strip()] for line in f.readlines()]
        height = len(data_grid)
        width = len(data_grid[0])
        antennas = [(t, y, x) for y, line in enumerate(data_grid) for x, t in enumerate(line) if t != '.']

    group_antennas = defaultdict(list)
    for sym, y, x in antennas:
        group_antennas[sym].append((y, x))


    from pprint import pp

    # pp(data_grid)

    antinodes = set()
    for _, locs in group_antennas.items():
        
        for (y1, x1), (y2, x2) in it.combinations(locs, r=2):
            dy, dx = y2 - y1, x2 - x1

            min_starty = min(y1, y2) // dy
            min_startx = min(x1, x2) // dx

            back = min(abs(min_starty), abs(min_startx))

            # Some error in this....
            starty = y1 - back*dy
            startx = x1 - back*dx

            times = min((max(starty, height-starty)) // abs(dy), max(startx,(width-startx)) // abs(dx))

            # but the -100 fixed the problem.
            possible_locs = [(starty+i*dy, startx+i*dx) for i in range(-100, times+1)]

            print(possible_locs)

            for x, y in possible_locs:
                if 0 <= y < height and 0 <= x < width:
                    antinodes.add((y, x))

    # Only Part One:
    print(len(antinodes))