import collections


grid = open('input.txt').readlines()
size = len(grid)

antennas = collections.defaultdict(list)
for x, l in enumerate(grid):
    for y, v in enumerate(l):
        if v != '.':
            antennas[v].append((x, y))


antinodes = set()
for t, locs in antennas.items():
    for i, (x1, y1) in enumerate(locs, 1):
        for x2, y2 in locs[i:]:
            dx, dy = x1 - x2, y1 - y2

            if 0 <= (x := x1 + dx) < size and 0 <= (y := y1 + dy) < size:
                antinodes.add((x, y))

            if 0 <= (x := x2 - dx) < size and 0 <= (y := y2 - dy) < size:
                antinodes.add((x, y))

print(len(antinodes))
