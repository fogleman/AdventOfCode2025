from functools import reduce
from itertools import combinations
from operator import or_, xor
from scipy.optimize import linprog
import fileinput
import re

machines = []
for line in fileinput.input():
    tokens = line.split()
    pattern = reduce(or_, [1 << i for i, c in enumerate(tokens[0][1:-1]) if c == '#'])
    buttons = tuple(tuple(map(int, re.findall(r'\d+', token))) for token in tokens[1:-1])
    masks = tuple(reduce(or_, [1 << int(i) for i in b]) for b in buttons)
    joltage = tuple(map(int, re.findall(r'\d+', tokens[-1])))
    machines.append((pattern, masks, buttons, joltage))

def count(pattern, masks):
    for n in range(1, len(masks) + 1):
        for combo in combinations(masks, n):
            if reduce(xor, combo) == pattern:
                return n

print(sum(count(m[0], m[1]) for m in machines))

def solve(buttons, joltage):
    c = [1] * len(buttons)
    A = [[int(i in b) for b in buttons] for i in range(len(joltage))]
    b = joltage
    return int(round(linprog(c, A_eq=A, b_eq=b, integrality=1).fun))

print(sum(solve(m[2], m[3]) for m in machines))
