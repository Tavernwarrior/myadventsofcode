
INPUT = 'input.txt'


APART_MULT = 1_000_000 # For part one set to 2


if __name__ == '__main__':

    with open(INPUT, 'r') as file:
        raw_data = file.readlines()
    
    width, heigth = len(raw_data[0])-1, len(raw_data)
    galaxies = [[(x, y) for x, sym in enumerate(row) if sym == '#'] for y, row in enumerate(raw_data)]

    empty_rows = [i for i, row in enumerate(galaxies) if not row]
    empty_cols = list(sorted(set(range(width)).difference(x for row in galaxies for (x, _) in row)))


    delta_row = [i*(APART_MULT-1) for i, (a, b) in enumerate(zip([0]+empty_rows, empty_rows+[heigth])) for _ in range(b-a)]
    delta_col = [i*(APART_MULT-1) for i, (a, b) in enumerate(zip([0]+empty_cols, empty_cols+[width])) for _ in range(b-a)]
    real_galaxies = [(x+delta_col[x], y+delta_row[y]) for row in galaxies if row for x, y in row]
    
    print(sum(sum(abs(x1-x2)+abs(y1-y2) for x2, y2 in real_galaxies[i+1:]) for i, (x1, y1) in enumerate(real_galaxies)))
