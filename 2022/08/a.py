
with open('input.txt') as file:
    grid = {(i, j): int(num) for i, line in enumerate(file) for j, num in enumerate(line.rstrip())}


m = max(x for (x, y) in grid)

tot = 0
for (x, y), num in grid.items():
    if x in [0, m] or y in [0, m]:
        tot += 1
        continue
    if all(grid[x + i + 1, y] < num for i in range(m - x)):
        tot += 1
    elif all(grid[x - i, y] < num for i in range(x, 0, -1)):
        tot += 1
    elif all(grid[x, y + i + 1] < num for i in range(m - y)):
        tot += 1
    elif all(grid[x, y - i] < num for i in range(y, 0, -1)):
        tot += 1

print(tot)
