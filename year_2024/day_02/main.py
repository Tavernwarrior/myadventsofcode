if __name__ == '__main__':

    with open('input') as f:
        reports = [[int(level) for level in line.strip().split(' ')] for line in f.readlines()]

    def test_report(report):
        delta = [a - b for a, b in zip(report[:-1], report[1:])]
        if 0 in delta: return False

        max_ = max(delta)
        min_ = min(delta)
        return abs(max_) < 4 and abs(min_) < 4 and min_//abs(min_) == max_//abs(max_)

    print(sum(test_report(report) or any(test_report(report[:i]+report[i+1:]) for i in range(len(report))) for report in reports))