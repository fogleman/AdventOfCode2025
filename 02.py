import fileinput
import re

numbers = list(map(int, re.findall(r'\d+', next(fileinput.input()))))

p1 = p2 = 0
for a, b in zip(numbers[::2], numbers[1::2]):
    for x in range(a, b + 1):
        s = str(x); n = len(s)
        p1 += x * (s[:n // 2] == s[n // 2:])
        p2 += x * any(all(s[:k] == s[i:i+k] for i in range(k, n, k)) for k in range(1, n))

print(p1)
print(p2)
