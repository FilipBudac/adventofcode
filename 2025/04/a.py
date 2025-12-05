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

def count_adjs(x, y, grid):
    return sum(grid.get(f(x, y)) != '@' for f in funcs)

print(sum(v == '@' and count_adjs(x, y, grid) > 4 for (x, y), v in grid.items()))
