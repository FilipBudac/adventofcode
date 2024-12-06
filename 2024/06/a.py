MOVE = {
    '^': lambda x, y: (x - 1, y),
    '>': lambda x, y: (x, y + 1),
    '<': lambda x, y: (x,  y - 1),
    'v': lambda x, y: (x + 1, y),
}
DIRS = {'^': '>', '>': 'v', 'v': '<',  '<': '^'}


def patrol(grid, cur):
    dir_ = grid[cur]

    seen = set()
    while True:
        if grid.get(MOVE[dir_](*cur)) == '#':
            dir_ = DIRS[dir_]
        else:
            seen.add(cur)
            cur = MOVE[dir_](*cur)

        if grid.get(cur) is None:
            return seen


grid = {(i, j): char for i, line in enumerate(open('input.txt')) for j, char in enumerate(line.rstrip())}
start = next((a, b) for (a, b), ch in grid.items() if ch == '^')

print(len(patrol(grid, start)))
