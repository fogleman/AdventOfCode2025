import fileinput
import re

numbers = list(map(int, re.findall(r'\d+', next(fileinput.input()))))

p1 = p2 = 0
for a, b in zip(numbers[::2], numbers[1::2]):
    for x in range(a, b + 1):
        s = str(x)
        n = len(s)
        i = n // 2
        if s[:i] == s[i:]:
            p1 += x
        for k in range(1, i + 1):
            if all(s[:k] == s[j:j+k] for j in range(0, n, k)):
                p2 += x
                break

print(p1)
print(p2)
