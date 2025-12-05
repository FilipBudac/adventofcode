funcs = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x, y - 1),

    lambda x, y: (x + 1, y + 1),
    lambda x, y: (x - 1, y - 1),
    lambda x, y: (x + 1, y - 1),
    lambda x, y: (x - 1, y + 1),
]

grid = {(i, j): char for i, line in enumerate(open('input.txt')) for j, char in enumerate(line.rstrip())}

def count_adjs(x, y, grid, removed):
    return sum(grid.get(f(x, y)) != '@' or f(x, y) in removed for f in funcs)


def count_rolls(grid, removed):
    count_ = len(removed)

    rolls = 0
    for (x, y), v in grid.items():
        if v == '@' and count_adjs(x, y, grid, removed) > 4:
            rolls += 1
            removed.add((x, y))

    return rolls - count_

rolls = 0
removed = set()
while True:
    rolls_ = count_rolls(grid, removed)
    if rolls_ == 0:
        break
    rolls += rolls_

print(rolls)