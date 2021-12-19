from itertools import starmap, product

BEACONS_BOUND = 12


negations = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (-x, y, z),
    lambda x, y, z: (x, -y, z),
    lambda x, y, z: (x, y, -z),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (-x, -y, -z),
]

rotations = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (x, z, y),
    lambda x, y, z: (z, y, x),
    lambda x, y, z: (y, x, z),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (z, x, y),
]


def get_scanners():
    with open("input.txt") as f:
        chunks = f.read().split('\n\n')
        scanners = [set(tuple(map(int, line.split(","))) for line in chunk.split('\n')[1:]) for chunk in chunks]
    return scanners


def main():
    scanners = get_scanners()

    found_scanners = [0]
    scanner_positions = [(0, 0, 0)] * len(scanners)
    unvisited_scanners = set(range(1, len(scanners)))
    while found_scanners:
        i = found_scanners.pop()
        for j in list(unvisited_scanners):
            if j in found_scanners:
                continue
            for negate, rotate in product(negations, rotations):
                scanner = set(starmap(negate, starmap(rotate, scanners[j])))
                for (x_1, y_1, z_1), (x_2, y_2, z_2) in product(scanners[i], scanner):
                    delta_x, delta_y, delta_z = x_1 - x_2, y_1 - y_2, z_1 - z_2
                    moved_scanner = {(x + delta_x, y + delta_y, z + delta_z) for x, y, z in scanner}
                    if len(scanners[i].intersection(moved_scanner)) >= BEACONS_BOUND:
                        scanners[j] = moved_scanner
                        scanner_positions[j] = (delta_x, delta_y, delta_z)
                        unvisited_scanners.remove(j)
                        found_scanners.append(j)
                        break

    max_distance = 0
    for (x_1, y_1, z_1), (x_2, y_2, z_2) in product(scanner_positions, scanner_positions):
        max_distance = max(max_distance, abs(x_1 - x_2) + abs(y_1 - y_2) + abs(z_1 - z_2))

    print(max_distance)


if __name__ == '__main__':
    main()
