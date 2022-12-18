def neighbors(x, y, z):
    return (x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)


with open('input.txt') as file:
    cubes = [tuple(map(int, l.rstrip().split(','))) for l in file]

cubes = {c: sum(n not in cubes for n in neighbors(*c)) for c in cubes}

print(sum(cubes.values()))
