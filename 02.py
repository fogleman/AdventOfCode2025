import fileinput

pairs = list(fileinput.input())[0].strip().split(',')
pairs = [tuple(map(int, p.split('-'))) for p in pairs]

p1 = 0
p2 = 0
for a, b in pairs:
    for x in range(a, b + 1):
        s = str(x)
        i = len(s) // 2
        if s[:i] == s[i:]:
            p1 += x
        for n in range(1, len(s) // 2 + 1):
            tokens = [s[i:i+n] for i in range(0, len(s), n)]
            if all(t == tokens[0] for t in tokens):
                p2 += x
                break

print(p1)
print(p2)
