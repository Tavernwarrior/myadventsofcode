import enum


INPUT = 'input.txt'


class Direction(enum.Enum):
    NONE = -1
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class TileEnum(enum.Enum):
    VERTICAL = '|'
    HORIZONTAL = '-'
    LBEND = 'L'
    JBEND = 'J'
    SBEND = '7'
    FBEND = 'F'
    GROUND = '.'
    START = 'S'


connections = {
    TileEnum.VERTICAL: (2, -1, 0, -1),
    TileEnum.HORIZONTAL: (-1, 3, -1, 1),
    TileEnum.LBEND: (1, 0, -1, -1),
    TileEnum.JBEND: (3, -1, -1, 0),
    TileEnum.SBEND: (-1, -1, 3, 2),
    TileEnum.FBEND: (-1, 2, 1, -1),
    }


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def at(map, x, y):
    return map[x][y]


def new_pos(cur, dir):
    delta = directions[dir.value]
    return cur[0]+delta[0], cur[1]+delta[1]


def invert_dir(dir):
    return Direction((dir.value+2)%4)


def next_dir(tile, dir):
    return Direction(connections[tile][dir.value])


def calculate_next(pos, dir):
    next_pos = new_pos(pos, dir)
    source_dir = invert_dir(dir)
    next_d = next_dir(at(map, *next_pos), source_dir)
    return next_pos, next_d


def color_neighbours(y, x, cnt, color_map):
    queue = [(y, x)]
    colored = 0
    while len(queue) > 0:
        y_, x_ = queue.pop(0)
        if 0 <= x_ < len(color_map[0]) and 0 <= y_ < len(color_map) and at(color_map, y_, x_) == -1:
            color_map[y_][x_] = cnt
            colored += 1
            queue.extend((y+dy, x+dx) for dy, dx in directions)
    return colored


def is_inside(x, area_row, sym_row):
    tiles = [sym for area, sym in zip(area_row[:x], sym_row[:x]) if area == 0 and sym not in (TileEnum.GROUND, TileEnum.HORIZONTAL)]
    last_tile = None
    cnt = 0
    for tile in tiles:
        match last_tile, tile:
            case _, TileEnum.VERTICAL:
                cnt += 1
            case None, t:
                last_tile = t
            case (TileEnum.LBEND, TileEnum.SBEND) | (TileEnum.FBEND, TileEnum.JBEND):
                cnt += 1
                last_tile = None
            case _:
                last_tile = None
    return (cnt%2) == 1


if __name__ == '__main__':
    with open(INPUT, 'r') as file:
        map = [[TileEnum(c) for c in line[:-1]] for line in file]

    area_map = [[-1 for _ in row] for row in map]  # Part Two

    starty, startx = next((y, x) for y, row in enumerate(map) for x, sym in enumerate(row) if sym == TileEnum.START)
    start_dirs = [(i, y, x) for i, (dy, dx) in enumerate(directions) if connections[at(map,y:=starty+dy, x:=startx+dx)][i] != -1]

    map[starty][startx] = next(tile for tile, con in connections.items() if all(con[i] != -1 for i, *_ in start_dirs))

    area_map[starty][startx] = 0
    current = [((y, x), invert_dir(next_dir(at(map, y, x), Direction(i)))) for i, y, x in start_dirs]
    step = 1
    while current[0][0] != current[1][0]:
        # for part two
        for (y, x), _ in current:
            area_map[y][x] = 0
        step += 1
        current = [calculate_next(pos, dir) for pos, dir in current]
    
    area_map[current[0][0][0]][current[0][0][1]] = 0

    print(f'Part One: {step}')


    marker = 2
    inside_num = 0
    for y, (sym_row, area_row) in enumerate(zip(map, area_map)):
        for x, area in enumerate(area_row):
            if area != -1:
                continue
            inside = is_inside(x, area_row, sym_row)
            if inside:
                inside_num += color_neighbours(y, x, -marker, area_map)
            else:
                color_neighbours(y, x, marker, area_map)
            marker += 1
    
    def print_inside_map():
        for y, (sym_row, area_row) in enumerate(zip(map, area_map)):
            for x, (sym, area) in enumerate(zip(sym_row, area_row)):
                print(int(is_inside(x, area_row, sym_row)) if area != 0 else 2, end='')
            print()
    
    # print_inside_map()
    print(f'Part Two: {inside_num}')
