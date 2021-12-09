import operator
from functools import reduce


def get_heightmap():
    with open('input.txt') as f:
        heightmap = [list(list(map(int, line.strip()))) for line in f.readlines()]

    return heightmap


def collect_neighbours(point, heightmap):
    x_steps = [-1, 0, 1, 0]
    y_steps = [0, 1, 0, -1]
    x, y = point

    neighbours = []
    for step in range(len(x_steps)):
        n_x = x + x_steps[step]
        n_y = y + y_steps[step]
        if 0 <= n_x < len(heightmap) and 0 <= n_y < len(heightmap[x]) and heightmap[n_x][n_y] != 9:
            neighbours.append((n_x, n_y))

    return neighbours


def get_basin_size(point, heightmap, checked_points):
    queue = [point]
    basin_size = 0
    while queue:
        point = queue.pop(0)
        if point in checked_points:
            continue
        basin_size += 1
        checked_points.add(point)
        queue.extend(collect_neighbours(point, heightmap))

    return basin_size


def main():
    res = []
    checked_points = set()

    heightmap = get_heightmap()
    for x in range(len(heightmap)):
        for y in range(len(heightmap[x])):
            neighbour_values = [heightmap[x][y] for x, y in collect_neighbours((x, y), heightmap)]
            if not neighbour_values:
                continue
            if min(neighbour_values) > heightmap[x][y]:
                basin = get_basin_size((x, y), heightmap, checked_points)
                res.append(basin)

    print(reduce(operator.mul, sorted(res)[-3:], 1))


if __name__ == '__main__':
    main()
