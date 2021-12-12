from collections import defaultdict
from typing import List, Dict


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


# backtracking
def _get_all_paths(
        cave_map: Dict[str, list],
        visited: Dict[str, bool],
        cave: str
) -> int:
    if cave == END:
        return 1

    # mark only lower case caves as visited! not all caves
    if cave.islower():
        visited[cave] = True

    count = 0
    neighbours = cave_map.get(cave)
    for neighbour in neighbours:
        # don't fall twice in the same small cave(hole)
        if neighbour in visited:
            continue
        # don't let modify the same visited in every recursion
        count += _get_all_paths(cave_map, dict(visited), neighbour)
    return count


def get_all_paths(cave_map: Dict[str, list]) -> int:
    visited = {}
    return _get_all_paths(cave_map, visited, START)


def main():
    paths = get_paths()
    cave_map = create_cave_map(paths)
    print(get_all_paths(cave_map))


if __name__ == '__main__':
    main()
