import fileinput
import re

total = 0
for line in fileinput.input():
    if 'x' not in line:
        continue
    numbers = list(map(int, re.findall(r'\d+', line)))
    w, h = numbers[:2]
    count = sum(numbers[2:])
    total += count * 9 <= w * h
print(total)
