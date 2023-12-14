import sys
from functools import cache


@cache
def rec_fish(start, days):
    return sum(rec_fish(9, days - day) for day in range(start, days, 7)) + 1


if __name__ == "__main__":
    num_days = int(sys.argv[1])

    with open("input.txt", "r") as f:
        data = f.readline().split(",")

    print(sum(rec_fish(int(fish), num_days) for fish in data ))