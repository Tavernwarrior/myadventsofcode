
SIZE = 10

def neighbours(x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (x == y == 0):
                yield x+i, y+j


def increase_energy(field, x, y):
    if x not in range(0, SIZE) or y not in range(0, SIZE):
        return 

    field[y][x] += 1
    if field[y][x] == 10:
        for nx, ny in neighbours(x, y):
            increase_energy(field, nx, ny)


def octo_step(field):
    for x in range(SIZE):
        for y in range(SIZE):
            increase_energy(field, x, y)

    flashes = 0

    for x in range(SIZE):
        for y in range(SIZE):
            if field[y][x] > 9:
                field[y][x] = 0
                flashes += 1

    return flashes

def octo_sim(start_field, steps):
    flash_count = 0
    for _ in range(steps):
        flash_count += octo_step(start_field)
    return flash_count


def octo_super_flash(start_field):
    flash_count = 0
    step = 0
    while flash_count < 100:
        if step == 388:
            print(start_field)
        flash_count = octo_step(start_field)
        step += 1
    return step

def load_input():
    with open("input.txt", "r") as f:
        data = [[int(n) for n in line.strip()] for line in f.readlines()]
    return data