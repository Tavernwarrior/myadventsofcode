from pprint import pp

if __name__ == '__main__':

    with open('input') as f:
        lines = [line.strip() for line in f.readlines()]
        divider = lines.index('')

        rules = [[int(x) for x in line.split('|')] for line in lines[:divider]]
        updates = [[int(x) for x in line.split(',')] for line in lines[divider+1:]]

    # Doesn't work for the example input.
    order = {}
    for x, y in rules:
        if x in order:
            order[x].add(y)
        else:
            order[x] = {y,}

    def break_rule(xs, x):
        return any(y in order[x] for y in xs)
    
    # Part One
    res = sum(up[len(up)//2] for up in updates if not any(break_rule(up[:i], up[i]) for i in range(1, len(up))))
    pp(res)


    def correct(li):
        i = 0
        while i < len(li):
            failed_at = next((j for j, y in enumerate(li[:i]) if y in order[li[i]]), None)
            if failed_at is not None:
                li[i], li[failed_at] = li[failed_at], li[i]
                i = failed_at
            i += 1
        return li


    # Part Two
    pp(sum(correct(up)[len(up)//2] for up in updates) - res)