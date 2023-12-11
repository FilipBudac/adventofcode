import itertools


with open('input.txt') as file:
    grid = {(i, j): ch for i, line in enumerate(file) for j, ch in enumerate(line.rstrip())}

x_max = max(x for x, _ in grid)
y_max = max(y for y, _ in grid)

galaxies = {pos for pos, val in grid.items() if val == '#'}

x_galaxies = {x for x, _ in galaxies}
y_galaxies = {y for _, y in galaxies}

e_rows = {x for x in range(x_max) if x not in x_galaxies}
e_cols = {y for y in range(y_max) if y not in y_galaxies}

paths = []
for (x, y), (nx, ny) in itertools.combinations(galaxies,2):
    path = 0
    for r in range(min(x, nx), max(x, nx)):
        path += 1000000 if r in e_rows else 1

    for c in range(min(y, ny), max(y, ny)):
        path += 1000000 if c in e_cols else 1

    paths.append(path)

print(sum(paths))
