import fileinput

grid = [list(line.strip()) for line in fileinput.input()]
w, h = len(grid[0]), len(grid)

total = 0
while True:
    done = True
    for y in range(h):
        for x in range(w):
            if grid[y][x] != '@':
                continue
            count = 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx or dy:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or ny < 0 or nx >= w or ny >= h:
                            continue
                        count += grid[ny][nx] == '@'
            if count < 4:
                total += 1
                grid[y][x] = '.'
                done = False
    if done:
        break
print(total)
