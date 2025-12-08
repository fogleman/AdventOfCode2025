import fileinput

points = [tuple(map(int, x.split(','))) for x in fileinput.input()]

def distance2(a, b):
    x0, y0, z0 = a
    x1, y1, z1 = b
    dx, dy, dz = x1 - x0, y1 - y0, z1 - z0
    return dx * dx + dy * dy + dz * dz

groups = set([frozenset([p]) for p in points])
edges = set()
for k in range(1000000):
    best = (1e9, None)
    for i, a in enumerate(points):
        for b in points[i+1:]:
            d2 = distance2(a, b)
            if d2 < best[0] and (a, b) not in edges:
                best = (d2, (a, b))
    edge = best[-1]
    print(k, edge, len(groups))
    edges.add(edge)
    a, b = edge
    ag = min(g for g in groups if a in g)
    bg = min(g for g in groups if b in g)
    if ag != bg:
        g = ag | bg
        groups.remove(ag)
        groups.remove(bg)
        groups.add(g)
        if len(groups) == 1:
            print(a[0] * b[0])
            break

# def connected(p, seen):
#     if p in seen:
#         return
#     seen.add(p)
#     for a, b in edges:
#         if a == p:
#             connected(b, seen)
#         if b == p:
#             connected(a, seen)

# groups = set()
# for p in points:
#     seen = set()
#     connected(p, seen)
#     seen = tuple(sorted(seen))
#     groups.add(seen)

# lengths = [len(group) for group in groups]
# lengths.sort()
# print(lengths[-1] * lengths[-2] * lengths[-3])
