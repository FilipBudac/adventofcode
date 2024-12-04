funcs1 = [
    lambda x, y: (x + 1, y + 1),
    lambda x, y: (x - 1, y - 1),
    lambda x, y: (x - 1, y - 1),
]

funcs2 = [
    lambda x, y: (x - 1, y + 1),
    lambda x, y: (x + 1, y - 1),
    lambda x, y: (x + 1, y - 1),
]


def compose_word(x, y, grid, funcs):
    word = ''
    for func in funcs:
        x, y = func(x, y)
        word += grid.get((x, y), '')
    return word


def search(x, y, grid):
    return all(compose_word(x, y, grid, funcs) in ('MAS', 'SAM') for funcs in (funcs1, funcs2))


with open('input.txt') as f:
    grid = {(i, j): char for i, line in enumerate(f) for j, char in enumerate(line.rstrip())}


print(sum(search(x, y, grid) for (x, y), _ in grid.items()))
