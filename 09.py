from collections import defaultdict
import fileinput

points = [tuple(map(int, line.split(','))) for line in fileinput.input()]

def area(a, b):
    ax, ay = a
    bx, by = b
    dx, dy = abs(ax - bx) + 1, abs(ay - by) + 1
    return dx * dy

print(max(area(a, b) for a in points for b in points))

xs = sorted(set(x for x, y in points))
ys = sorted(set(y for x, y in points))
ps = sorted(set(v for x in xs for v in (x - 1, x, x + 1)))
qs = sorted(set(v for y in ys for v in (y - 1, y, y + 1)))
pl = {x: i for i, x in enumerate(ps)}
ql = {y: i for i, y in enumerate(qs)}

def compress(x, y):
    return (pl[x], ql[y])

def perimeter(points):
    result = set()
    for i in range(len(points)):
        j = (i + 1) % len(points)
        ax, ay = points[i]
        bx, by = points[j]
        dx, dy = bx - ax, by - ay
        sx = dx // abs(dx) if dx else 0
        sy = dy // abs(dy) if dy else 0
        if sx:
            for x in range(ax, bx + sx, sx):
                result.add((x, ay))
        else:
            for y in range(ay, by + sy, sy):
                result.add((ax, y))
    return result

def fill(points):
    x0, x1 = min(x for x, y in points), max(x for x, y in points)
    y0, y1 = min(y for x, y in points), max(y for x, y in points)
    x0, x1 = x0 - 1, x1 + 1
    y0, y1 = y0 - 1, y1 + 1
    points = set(points)
    result = set([(x0, y0)])
    Q = [(x0, y0)]
    while Q:
        x, y = Q.pop()
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx and dy:
                    continue
                nx, ny = x + dx, y + dy
                if nx < x0 or ny < y0 or nx > x1 or ny > y1:
                    continue
                if (nx, ny) in result:
                    continue
                if (nx, ny) in points:
                    continue
                Q.append((nx, ny))
                result.add((nx, ny))
    return result

def dense(points):
    points = [compress(*p) for p in points]
    points = perimeter(points)
    points = fill(points)
    return points

def valid(outside, a, b):
    ax, ay = a
    bx, by = b
    x0, x1 = min(ax, bx), max(ax, bx)
    y0, y1 = min(ay, by), max(ay, by)
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if (x, y) in outside:
                return False
    return True

outside = dense(points)

def valid_area(a, b):
    if not valid(outside, a, b):
        return 0
    ax, ay = a
    bx, by = b
    ax, ay = ps[ax], qs[ay]
    bx, by = ps[bx], qs[by]
    dx, dy = abs(ax - bx) + 1, abs(ay - by) + 1
    return dx * dy

compressed = [compress(*p) for p in points]
print(max(valid_area(a, b) for a in compressed for b in compressed))
