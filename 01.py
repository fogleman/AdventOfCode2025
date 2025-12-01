import fileinput

p1, p2, x = 0, 0, 50
for line in fileinput.input():
    for i in range(int(line[1:])):
        x = (x + [-1, 1][line[0] == 'R']) % 100
        p2 += x == 0
    p1 += x == 0

print(p1)
print(p2)
