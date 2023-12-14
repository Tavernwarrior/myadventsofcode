import sys


file = sys.argv[1]

with open(file, "r") as f:
    lines = f.readlines()
    
num_size = len(lines[0]) - 1
size = len(lines)
count = [0]*num_size

for num in lines:
    for i, bit in enumerate(num[:-1]):
        count[i] += int(bit)

max = 2**num_size-1
gamma = sum((n > size//2) * 2**i for i, n in enumerate(reversed(count)))
epsilon = max - gamma

print(gamma, epsilon)
print(gamma * epsilon)

oxygen = int(lines[0].strip())
co2 = oxygen

for num in lines[1:]:
    b = int(num.strip())
    if oxygen & gamma > b & gamma:
        oxygen = b
    if co2 & epsilon < b & epsilon:
        co2 = b