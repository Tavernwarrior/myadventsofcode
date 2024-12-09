from operator import mul, add
from pprint import pp


if __name__ == '__main__':

    with open('input') as f:
        data = [line.strip().split(':') for line in f.readlines()]
        equations = [(int(res), tuple(int(a) for a in right.split())) for res, right in data]

    concat = lambda x, y: int(str(x)+str(y))

    # Version without match-case
    def num_combinations_rec(left, right):
        if not right or right[0] > left:
            return 0
        if len(right) == 1:
            return right[0] == left
        else:
            combinations = 0
            for op in [add, mul, concat]:
                combinations += num_combinations_rec(left, (op(right[0], right[1]), *right[2:]))
            return combinations


    def num_combinations(left, right, ops):
        match right:
            case (x, ):
                return x == left
            case (x, y, *args) if x <= left:
                return sum(num_combinations(left, (op(x, y),*args), ops) for op in ops)
            case _:
                return 0


    # pp(sum(res for res, right in equations if num_combinations_rec(res, right)))

    # Part One:
    pp(sum(res for res, right in equations if num_combinations(res, right, [add, mul])))

    # Part Two:
    pp(sum(res for res, right in equations if num_combinations(res, right, [add, mul, concat])))