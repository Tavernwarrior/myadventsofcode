from collections import Counter


def parse_point(txt):
    return tuple(int(x.strip()) for x in txt.split(","))


def parse_line(txt):
    return tuple(parse_point(p) for p in txt.split(" -> "))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = [ parse_line(line) for line in f.readlines()]
    
    count = Counter()
    for (x1, y1), (x2, y2) in data:
        if x1 == x2:
            count.update((x1, y) for y in range(y1, y2 + (1 if y2 > y1 else -1), 1 if y2 > y1 else -1))
        elif y1 == y2:
            count.update((x, y1) for x in range(x1, x2 + (1 if x2 > x1 else -1), 1 if x2 > x1 else -1))
        elif abs(x2-x1) == abs(y2-y1):
            x_off = 1 if x2 > x1 else -1
            y_off = 1 if y2 > y1 else -1
            for i in range(abs(x2-x1)+1):
                count[(x1 + x_off*i, y1 + y_off*i)] += 1

    print(sum(int(count[k]>1) for k in count))
