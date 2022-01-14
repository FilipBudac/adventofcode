with open('input.txt') as file:
    grid = [list(line.strip()) for line in file]

height, width = len(grid), len(grid[0])

trees = x = y = 0
while x < height:
    if grid[x][y] == '#':
        trees += 1
    x += 1
    y += 3
    y %= width

print(trees)
