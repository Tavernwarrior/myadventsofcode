import sys 


def error(nums, x):
    return sum( abs(num - x) for num in nums)

def median(nums):
    return sorted(nums)[len(nums)//2]


def find_min(nums):
    best = median(nums)
    return error(nums, best), best


def gauss_error(nums, x):
    def gauss(n):
        return (n*n + n)//2
    return sum(gauss(abs(num - x)) for num in nums)


def gauss_min(nums):
    best = round((sum(nums) - median(nums))/len(nums))
    return gauss_error(nums, best), best

def gauss_min2(nums):
    best = round((sum(nums) - median(nums)//2)/len(nums))
    return gauss_error(nums, best), best

def find_min_slow(nums):
    max_ = max(nums)
    min_ = min(nums)
    return min(((error(nums, x), x) for x in range(min_, max_)), key=lambda p: p[0])


def load_input():
    with open("input.txt", "r") as f:
        data = [int(n) for n in f.readline().split(",")]
    return data

if __name__ == "__main__":

    data = load_input()
    
    print(find_min(data))