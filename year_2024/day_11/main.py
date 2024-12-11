if __name__ == '__main__':

    with open('input') as f:
        stones  = [int(num) for num in f.readline().strip().split()]


    def blink(num):
        if num == 0:
            return [1]
        elif (n := len(s := str(num))) % 2 == 0:
            return [int(s[:n//2]), int(s[n//2:])]
        else:
            return [num * 2024]


    def blinking(num, cache, blinks=25):
        if (num, blinks) in cache:
            return cache[(num, blinks)]
        if blinks == 0:
            return 1
        else:
            result = sum(blinking(res, cache, blinks-1) for res in blink(num))
            cache[(num, blinks)] = result
            return result

    mycache = {}

    # Part One
    print(sum(blinking(stone, mycache, 25) for stone in stones))

    # Part Two
    print(sum(blinking(stone, mycache, 75) for stone in stones))