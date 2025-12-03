import fileinput

lines = [line.rstrip() for line in fileinput.input()]

for n in [2, 12]:
    total = 0
    for line in lines:
        s = ''
        for i in range(n):
            x = max(line[:len(line) - n + i + 1])
            line = line[line.index(x) + 1:]
            s += x
        total += int(s)
    print(total)
