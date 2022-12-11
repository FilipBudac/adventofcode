with open('input.txt') as file:
    grid = {(i, j): int(num) for i, line in enumerate(file) for j, num in enumerate(line.rstrip())}

tot = 0
size = max(x for (x, y) in grid)
for (x, y), num in grid.items():
    if (
        all(grid[x + i + 1, y] < num for i in range(size - x)) or
        all(grid[x, y + i + 1] < num for i in range(size - y)) or
        all(grid[x - i - 1, y] < num for i in range(x)) or
        all(grid[x, y - i - 1] < num for i in range(y))
    ):
        tot += 1

print(tot)
