from collections import Counter

INPUT = 'input.txt'


def part_equal(seq1, seq2):
    return all(a == b for a, b in zip(seq1, seq2))

def count_unequal(seq1, seq2):
    return sum(int(a != b) for a, b in zip(seq1, seq2))

def is_nearly_equal(seq1, seq2):
    most = Counter(count_unequal(a, b) for a, b in zip(seq1, seq2)).most_common()
    return all((v==1 and n==1) or v==0 for v, n in most) and (1, 1) in most

def find_reflection_smudge(grid):
    cnt = Counter(i for row in grid for i in range(1, len(row)) if part_equal(row[i:], reversed(row[:i]))).most_common()
    found = next((li for li, num in cnt if num == len(grid)-1), 0)
    if found != 0:
        return found, 0
    ver = next(i for i in range(1, len(grid)) if is_nearly_equal(grid[i:], reversed(grid[:i])))
    return 0, ver


def find_reflection(grid):
    cnt = Counter(i for row in grid for i in range(1, len(row)) if part_equal(row[i:], reversed(row[:i])))
    hor, num = cnt.most_common(1)[0]
    if cnt and num == len(grid):
        return hor, 0
    ver = next((i for i in range(1, len(grid)) if part_equal(grid[i:], reversed(grid[:i]))), -1)
    return 0, ver

if __name__ == '__main__':
    
    with open(INPUT, 'r') as file:
        dataset = []
        entry = []
        for line in file:
            if (sline := line.strip()) == '':
                dataset.append(entry)
                entry = []
            else:
                entry.append(sline)
        dataset.append(entry)


    def score(res):
        return res[0] + res[1]*100
    print(sum(score(find_reflection_smudge(data)) for data in dataset))
