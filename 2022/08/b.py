import functools

with open('input.txt') as file:
    grid = {(i, j): int(num) for i, line in enumerate(file) for j, num in enumerate(line.rstrip())}

m = max(x for (x, y) in grid)

tot = []
for (x, y), num in grid.items():
    if x in [0, m] or y in [0, m]:
        continue
    c = 4 * [0]
    for i in range(m - x):
        if grid[x + i + 1, y] >= num:
            c[0] += 1
            break
        c[0] += 1

    for i in range(x):
        if grid[x - i - 1, y] >= num:
            c[1] += 1
            break
        c[1] += 1

    for i in range(m - y):
        if grid[x, y + i + 1] >= num:
            c[2] += 1
            break
        c[2] += 1

    for i in range(y):
        if grid[x, y - i - 1] >= num:
            c[3] += 1
            break
        c[3] += 1
    tot.append(functools.reduce((lambda x, y: x * y), c))

print(max(tot))
