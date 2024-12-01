from collections import Counter


if __name__ == '__main__':
    with open('data.txt') as f:
        lines_raw = (line.strip().split('   ') for line in f.readlines())

        lines = [(int(a), int(b)) for a, b in lines_raw]

    a = [a for a, _ in lines]
    b = [b for _, b in lines]

    # Part 1
    print(sum(abs(a-b) for a, b in zip(sorted(a), sorted(b))))


    cnt_b = Counter(b)

    print(sum(_a*cnt_b[_a] for _a in a))
