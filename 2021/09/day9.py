import sys


def get_heightmap():
    with open('input.txt') as f:
        heightmap = [list(list(map(int, line.strip()))) for line in f.readlines()]

    return heightmap


def get_lowest_point(point, heightmap):
    x, y = point
    up = down = left = right = sys.maxsize

    size = len(heightmap)
    if x + 1 < size:
        up = heightmap[x + 1][y]
    if x - 1 >= 0:
        down = heightmap[x - 1][y]
    if y - 1 >= 0:
        left = heightmap[x][y - 1]
    if y + 1 < size:
        right = heightmap[x][y + 1]

    return heightmap[x][y] + 1 if min([up, down, left, right]) > heightmap[x][y] else None


def a():
    res = 0
    heightmap = get_heightmap()
    for x in range(len(heightmap)):
        for y in range(len(heightmap[x])):
            if lowest_point := get_lowest_point((x, y), heightmap):
                res += lowest_point
    print(res)


def main():
    a()


if __name__ == '__main__':
    main()
