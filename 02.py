import fileinput
import re

numbers = list(map(int, re.findall(r'\d+', next(fileinput.input()))))

p1 = p2 = 0
for a, b in zip(numbers[::2], numbers[1::2]):
    for x in range(a, b + 1):
        s = str(x); n = len(s); i = n // 2
        p1 += x * (s[:i] == s[i:])
        p2 += x * (s in (s + s)[1:-1])

print(p1)
print(p2)
