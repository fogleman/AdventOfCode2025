import fileinput

spans = []
values = []
for line in fileinput.input():
    if '-' in line:
        spans.append(list(map(int, line.split('-'))))
    elif line.strip():
        values.append(int(line))

print(sum(any(a <= x <= b for a, b in spans) for x in values))

merged = []
for a, b in sorted(spans):
    if merged and a <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], b)
    else:
        merged.append([a, b])

print(sum(b - a + 1 for a, b in merged))
