
if __name__ == '__main__':

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    with open('input') as f:
        grid = [[int(tile) for tile in line.strip()] for line in f.readlines()]

    def get(grid, y, x):
        return grid[y][x] if 0 <= y < len(grid) and 0 <= x < len(grid[0]) else -1

    def num_hiking_routes(y, x, grid, current, visited):
        if current == 9:
            if (y, x) not in visited and grid[y][x] == current:
                visited.add((y, x))
                return 1
            else:
                return 0
        else:
            return sum(num_hiking_routes(y+dy, x+dx, grid, current+1, visited) for dy, dx in directions if get(grid, y+dy, x+dx) == current+1)

    # Part One
    print(sum(num_hiking_routes(y, x, grid, 0, set()) for y, line in enumerate(grid) for x, tile in enumerate(line) if tile==0))

    def num_hiking_routes2(y, x, grid, current):
        if current == 9:
            return grid[y][x] == current
        else:
            return sum(num_hiking_routes2(y+dy, x+dx, grid, current+1) for dy, dx in directions if get(grid, y+dy, x+dx) == current+1)

    # Part Two
    print(sum(num_hiking_routes2(y, x, grid, 0) for y, line in enumerate(grid) for x, tile in enumerate(line) if tile==0))
