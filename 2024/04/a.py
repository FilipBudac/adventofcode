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


def compose_word(x, y, grid, func):
    word = grid.get((x, y))
    for _ in range(3):
        x, y = func(x, y)
        word += grid.get((x, y), '')
    return word


def search(x, y, grid):
    return sum(compose_word(x, y, grid, func) == 'XMAS' for func in funcs)


with open('input.txt') as f:
    grid = {(i, j): char for i, line in enumerate(f) for j, char in enumerate(line.rstrip())}


print(sum(search(x, y, grid) for (x, y), _ in grid.items()))
