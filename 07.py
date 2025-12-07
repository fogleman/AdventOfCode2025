import fileinput

grid = [line.rstrip() for line in fileinput.input()]
w, h = len(grid[0]), len(grid)

sx = 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == 'S':
            sx = x

xs = set([sx])

total = 0
for y in range(1, h):
    splitters = {x for x in range(w) if grid[y][x] == '^'}
    split_points = splitters & xs
    non_split_points = xs - split_points
    total += len(split_points)
    new_xs = non_split_points
    for x in split_points:
        new_xs.add(x - 1)
        new_xs.add(x + 1)
    xs = new_xs

print(total)

def count(x, y, memo):
    if y == h:
        return 1
    key = (x, y)
    if key in memo:
        return memo[key]
    if grid[y][x] == '^':
        result = count(x - 1, y + 1, memo) + count(x + 1, y + 1, memo)
        memo[key] = result
        return result
    result = count(x, y + 1, memo)
    memo[key] = result
    return result

memo = {}
print(count(sx, 0, memo))
