import collections
import operator


def gen(x, y, dx, dy, size, op):
    nx = op(x, dx)
    ny = op(y, dy)

    while 0 <= nx < size and 0 <= ny < size:
        yield nx, ny

        nx = op(nx, dx)
        ny = op(ny, dy)


grid = open('input.txt').readlines()
size = len(grid)

antennas = collections.defaultdict(list)
for x, l in enumerate(grid):
    for y, v in enumerate(l.rstrip()):
        if v != '.':
            antennas[v].append((x, y))

antinodes = set()
for t, locs in antennas.items():
    for i, (x1, y1) in enumerate(locs, 1):
        antinodes.add((x1, y1))
        for x2, y2 in locs[i:]:
            dx, dy = x1 - x2, y1 - y2
            antinodes.update(gen(x1, y1, dx, dy, size, operator.add))
            antinodes.update(gen(x2, y2, dx, dy, size, operator.sub))


print(len(antinodes))
