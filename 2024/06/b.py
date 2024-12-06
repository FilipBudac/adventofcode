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
            seen.add((*cur, dir_))
            cur = MOVE[dir_](*cur)

        if grid.get(cur) is None:
            return {(x, y) for x, y, _ in seen}

        if (*cur, dir_) in seen:
            return set()


grid = {(x, y): char for x, line in enumerate(open('input.txt')) for y, char in enumerate(line.rstrip())}

start = next((x, y) for (x, y), ch in grid.items() if ch == '^')
seen = patrol(grid, start)

print(sum(not patrol({**grid, (x, y): '#'}, start) for x, y in seen if (x, y) != start))
