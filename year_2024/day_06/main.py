from pprint import pp 

if __name__ == '__main__':

    with open('input') as f:
        lab = [list(line.strip()) for line in  f.readlines()]
        y, x = next((y, x) for y, line in enumerate(lab) for x, tile in enumerate(line) if tile == '^')
        dy, dx = -1, 0
        height = len(lab)
        width = len(lab[0])
        obs = {(y, x) for y, line in enumerate(lab) for x, tile in enumerate(line) if tile == '#'}


    def move_guard(y, x, dy, dx, obstacles, path):  # Returns True if no loop is found
        while 0 <= y < height and 0 <= x < width:
            if (y, x, dy, dx) in path:
                return False
            path.add((y, x, dy, dx))

            if 0 <= y+dy < height and 0 <= x+dx < width:
                if (y+dy,x+dx) in obstacles:
                    dy, dx = dx, -dy
                else:
                    y += dy
                    x += dx
            else:
                return True
        return True


    # Part Two (Brute Force)
    # print(sum(not move_guard(y, x, dy, dx, obs | {(y_, x_)}, set()) for y_, line in enumerate(lab) for x_, t in enumerate(line) if (y_, x_) != (y, x)))


    # Debugging: printing the labyrinth
    # move_guard(y, x, dy, dx, obs, path)
    # path_pos = {(y, x) for y, x, _, _ in path}
    # lab_test = [['#' if (y, x) in obs else ('X' if (y, x) in path_pos else '.')  for x, t in enumerate(line)] for y, line in enumerate(lab)]
    # pp(lab_test)


    path = set()
    move_guard(y, x, dy, dx, obs, path)

    # Part One
    print(len({(y, x) for y, x, _, _ in path}))

    possible_obstructions = {(y_+dy_, x_+dx_) for y_, x_, dy_, dx_ in path if (npos:=y_+dy_, x_+dx_) != (y, x)}

    #Part Two
    print(sum(not move_guard(y, x, dy, dx, obs | {obs_pos}, set()) for obs_pos in possible_obstructions))
