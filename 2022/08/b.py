import functools

with open('input.txt') as file:
    grid = {(i, j): int(num) for i, line in enumerate(file) for j, num in enumerate(line.rstrip())}

tot = []
size = max(x for (x, y) in grid)
for (x, y), num in grid.items():
    c = 4 * [0]
    for i in range(size - x):
        c[0] += 1
        if grid[x + i + 1, y] >= num:
            break
    for i in range(x):
        c[1] += 1
        if grid[x - i - 1, y] >= num:
            break
    for i in range(size - y):
        c[2] += 1
        if grid[x, y + i + 1] >= num:
            break
    for i in range(y):
        c[3] += 1
        if grid[x, y - i - 1] >= num:
            break
    tot.append(functools.reduce((lambda a, b: a * b), c))

print(max(tot))
