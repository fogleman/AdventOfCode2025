import fileinput
from functools import reduce
from operator import add, mul

grid = [line.replace('\n', ' ') for line in fileinput.input()]

w, h = len(grid[0]), len(grid)

value = 0
op = ''
total = 0
for x in range(w):
    if all(grid[y][x] == ' ' for y in range(h)):
        total += value
        value = 0
        op = ''
        continue
    if grid[h-1][x] != ' ':
        op = grid[h-1][x]
        if op == '*':
            value = 1
    num = []
    for y in range(h-1):
        num.append(grid[y][x])
    num = int(''.join(num))
    if op == '*':
        value *= num
    else:
        value += num
print(total)

# rows = []
# ops = []
# for line in fileinput.input():
#     try:
#         rows.append(list(map(int, line.split())))
#     except Exception:
#         ops = line.split()

# w, h = len(rows[0]), len(rows)

# total = 0
# for x in range(w):
#     op = ops[x]
#     values = [row[x] for row in rows]
#     if op == '+':
#         value = reduce(add, values)
#     else:
#         value = reduce(mul, values)
#     total += value
# print(total)
