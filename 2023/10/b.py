import matplotlib.path

DIRECT = {
    "J": {(0, -1): (-1, 0), (1, 0): (0, 1)},
    "F": {(0, 1): (1, 0), (-1, 0): (0, -1)},
    "7": {(0, 1): (-1, 0), (1, 0): (0, -1)},
    "L": {(0, -1): (1, 0), (-1, 0): (0, 1)},
}


CHECKS = {
    (0, 1): {'7', 'F', '|'},
    (0, -1): {'J', 'L', '|'},
    (1, 0): {'7', 'J', '-'},
    (-1, 0): {'F', 'L', '-'},
}

def get_start_position(grid):
    return next(pos for pos, t in grid.items() if t == 'S')

def get_start_direction(grid, x, y):
    for (dx, dy), pipes in CHECKS.items():
        if grid.get((x + dx, y + dy)) in pipes:
            return dx, dy


def find_loop(grid):
    sx, sy = get_start_position(grid)
    dx, dy = get_start_direction(grid, sx, sy)

    x, y = (sx + dx, sy + dy)

    loop = [(x, y)]
    while grid[x, y] != 'S':
        loop.append((x, y))
        if grid[x, y] in DIRECT:
            dx, dy = DIRECT[grid[x, y]][dx, dy]
        x, y = (x + dx, y + dy)

    return loop


with open('input.txt') as file:
    grid = {(j, i): ch for i, line in enumerate(file.readlines()[::-1]) for j, ch in enumerate(line.rstrip())}

loop = find_loop(grid)
path = matplotlib.path.Path(loop)
print(sum(pos not in loop and path.contains_point(pos) for pos in grid))
