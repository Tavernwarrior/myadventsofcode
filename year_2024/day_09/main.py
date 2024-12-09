if __name__ == '__main__':
    with open('input') as f:
        map = f.readline().strip()

        blocks = [-1 if i%2 == 1 else i//2 for i, a in enumerate(map) for _ in range(int(a))]

    blocks_clean = [b for b in blocks if b != -1]

    rev_blocks_value = reversed(blocks_clean)

    # Part One
    print(sum(i*blocks[i] if blocks[i] != -1 else i*next(rev_blocks_value) for i in range(len(blocks_clean))))

    block_frag = [(-1 if i%2 == 1 else i//2, int(a)) for i, a in enumerate(map)]

    rev_blocks = ((i, b) for i, b in enumerate(reversed(block_frag)) if b[0] != -1)

    new_block_frag = block_frag.copy()

    # Debug
    # print(''.join([str(i) if i != -1 else '.' for i, a in new_block_frag for _ in range(a)]))

    for k, b in rev_blocks:
        free = next(((i, bl) for i, bl in enumerate(new_block_frag) if bl[0] == -1 and bl[1] >= b[1]), None)
        loc = next(i for i, (id, _) in enumerate(new_block_frag) if id == b[0])

        if free is not None and free[0] < loc:
            new_block_frag[loc] = (-1, b[1])
            new_block_frag[free[0]] = (-1, free[1][1] - b[1])
            new_block_frag.insert(free[0], b)

    # Part Two
    print(sum(j*m if m!=-1 else 0 for j, m in enumerate(i for i, a in new_block_frag for _ in range(a))))

    # Debug
    # print(''.join([hex(i)[-1] if i != -1 else '.' for i, a in new_block_frag for _ in range(a)]))