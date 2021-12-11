from typing import Dict, Set

STEPS = 100


def get_energy_map() -> Dict[tuple, int]:
    with open('input.txt') as f:
        energy_map = {(i, j): int(num) for i, line in enumerate(f.readlines()) for j, num in enumerate(list(line.strip()))}
    return energy_map


def print_energy_map(energy_map: Dict[tuple, int]):
    res = ''
    for i, (point, energy) in enumerate(energy_map.items()):
        if i % 10 == 0:
            res += '\n'
        res += f'{energy},'
    print(res)


def collect_neighbours(cur_point: tuple, energy_map: Dict[tuple, int]) -> Dict[tuple, int]:
    neighbour_deltas = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
    x, y = cur_point

    neighbours = {}
    for neighbour_delta in neighbour_deltas:
        d_x, d_y = neighbour_delta
        neighbour_point = (x + d_x, y + d_y)

        if neighbour_point in energy_map and energy_map[neighbour_point] > 0:
            neighbours[neighbour_point] = energy_map[neighbour_point]

    return neighbours


def get_new_flashes(point: tuple, energy_map: Dict[tuple, int]):
    neighbours = collect_neighbours(point, energy_map)
    new_flashes = {point for point, energy in neighbours.items() if energy > 9}
    return new_flashes


def light_point(point: tuple, energy_map: Dict[tuple, int]):
    energy_map[point] = -1
    neighbours = collect_neighbours(point, energy_map)
    for n_point in neighbours.keys():
        energy_map[n_point] += 1


def progress(point: tuple, energy_map: Dict[tuple, int]):
    light_point(point, energy_map)
    return get_new_flashes(point, energy_map)


def increase_energy(energy_map: Dict[tuple, int]) -> Dict[tuple, int]:
    return {point: energy + 1 for point, energy in energy_map.items()}


def main():
    count = 0
    energy_map: Dict[tuple, int] = get_energy_map()
    for step in range(STEPS):
        energy_map: Dict[tuple, int] = increase_energy(energy_map)
        flashes: Set[tuple] = {point for point, energy in energy_map.items() if energy > 9}
        while flashes:
            new_flashes = progress(flashes.pop(), energy_map)
            flashes.update(new_flashes)
        for point, energy in energy_map.items():
            if energy == -1:
                count += 1
                energy_map[point] = 0
    print(count)


if __name__ == '__main__':
    main()
