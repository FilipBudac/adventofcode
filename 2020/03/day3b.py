from functools import reduce
from operator import mul

STEPS = (
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1)
)


def encountered_trees(x_step, y_step):
    trees = x = y = 0
    while x < height:
        if grid[x][y] == '#':
            trees += 1
        x += x_step
        y += y_step
        y %= width
    return trees


with open('input.txt') as file:
    grid = [list(line.strip()) for line in file]

height, width = len(grid), len(grid[0])

print(reduce(mul, [encountered_trees(x_step, y_step) for x_step, y_step in STEPS]))
