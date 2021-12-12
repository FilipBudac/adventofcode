from collections import defaultdict
from typing import List, Dict
from copy import copy


START = 'start'
END = 'end'


def get_paths() -> List[list]:
    with open('input.txt') as f:
        paths = [path.strip().split('-') for path in f.readlines()]
    return paths


def create_cave_map(paths: List[list]) -> Dict[str, list]:
    cave_map = defaultdict(list)

    for path in paths:
        start, end = path
        cave_map[start].append(end)
        cave_map[end].append(start)

    return cave_map


def get_neighbours(cave_map: Dict[str, list], neighbour: str) -> list:
    # start cave is no no!
    return [cave for cave in cave_map[neighbour] if cave != 'start']


def is_double_small_cave(visited: Dict[str, int]) -> bool:
    # if we fell in a small cave twice, at least don't make the same mistake twice
    return any(visits > 1 for cave, visits in visited.items())


def _get_all_paths(
        cave_map: Dict[str, list],
        visited,
        cave: str
) -> int:
    if cave == END:
        return 1

    if cave.islower():
        visited[cave] += 1

    count = 0
    neighbours = get_neighbours(cave_map, cave)
    for neighbour in neighbours:
        if neighbour in visited and is_double_small_cave(visited):
            continue
        count += _get_all_paths(cave_map, copy(visited), neighbour)
    return count


def get_all_paths(cave_map: Dict[str, list]) -> int:
    visited = defaultdict(int)
    return _get_all_paths(cave_map, visited, START)


def main():
    paths = get_paths()
    cave_map = create_cave_map(paths)
    print(get_all_paths(cave_map))


if __name__ == '__main__':
    main()
