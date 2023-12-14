
import sys


file = sys.argv[1]

horizontal = 0
vertical = 0
aim = 0

with open(file, "r") as f:
    inputs = [line.strip().split() for line in f.readlines()]
    
for inp in inputs:
    match (inp[0], int(inp[1])):
        case ("forward", n):
            horizontal += n
            vertical += n * aim
        case ("up", n):
            aim -= n
        case ("down", n):
            aim += n
            
print(horizontal, vertical)
print(horizontal * vertical)