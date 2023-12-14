def fold(points, axis, coord):
    return {(px if axis == "y" else coord - abs(coord - px), py if axis == "x" else coord - abs(coord - py)) for px, py in points}


def all_fold(points, folds):
    current = points
    for f in folds:
        current = fold(current, *f)
    return current


def matrix(points):
    xmax = max(points, key=lambda x: x[0])[0]
    ymax = max(points, key=lambda x: x[1])[1]
    mat = [["." for _ in range(xmax+1)] for _ in range(ymax+1)]
    for px, py in points:
        mat[py][px] = "#"
    return mat


def load_input(path="input.txt"):
    points = set()
    folds = []
    read_pt = True
    with open(path, "r") as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line == "":
                read_pt = False
                continue
            if read_pt:
                points.add(tuple(int(n) for n in stripped_line.split(",")))
            else:
                fold = stripped_line.split()[2].split("=")
                folds.append((fold[0], int(fold[1])))

    return points, folds            