import fileinput

p1 = 0
p2 = 0
x = 50

for line in fileinput.input():
    d = line[0]
    n = int(line[1:])
    for i in range(n):
        if d == 'L':
            x = (x - 1) % 100
        else:
            x = (x + 1) % 100
        if x == 0:
            p2 += 1
    if x == 0:
        p1 += 1

print(p1)
print(p2)
