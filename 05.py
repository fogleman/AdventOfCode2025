import fileinput

ranges = []
values = []
for line in fileinput.input():
    line = line.rstrip()
    if not line:
        continue
    elif '-' in line:
        a, b = map(int, line.split('-'))
        ranges.append((a, b))
    else:
        values.append(int(line))

total = 0
for value in values:
    if any(a <= value <= b for a, b in ranges):
        total += 1
print(total)

points = set()
for a, b in ranges:
    points.add(a)
    points.add(b)
points = list(sorted(points))

total = 0
seen = set()
for p, q in zip(points, points[1:]):
    d = q - p
    r = p + 1
    if p not in seen and any(a <= p <= b for a, b in ranges):
        total += 1
    seen.add(p)
    if q not in seen and any(a <= q <= b for a, b in ranges):
        total += 1
    seen.add(q)
    if r not in seen and any(a <= r <= b for a, b in ranges):
        total += d - 1
    seen.add(r)
print(total)
