from itertools import count

EAST = '>'
SOUTH = 'v'
EMPTY = '.'


def get_situation_map():
    with open("input.txt") as f:
        situation_map = [list(line.strip()) for line in f.readlines()]
    return situation_map


def move_east(situation_map, move_east_map, x_size, y_size):
    for x in range(x_size):
        for y in range(y_size):
            if situation_map[y][x] != EAST:
                continue
            X = (x + 1) % x_size
            if situation_map[y][X] == EMPTY:
                move_east_map[(x, y)] = (X, y)

    for (x1, y1), (x2, y2) in move_east_map.items():
        situation_map[y2][x2] = EAST
        situation_map[y1][x1] = EMPTY


def move_south(situation_map, move_south_map, x_size, y_size):
    for x in range(x_size):
        for y in range(y_size):
            if situation_map[y][x] != SOUTH:
                continue
            Y = (y + 1) % y_size
            if situation_map[Y][x] == EMPTY:
                move_south_map[(x, y)] = (x, Y)

    for (x1, y1), (x2, y2) in move_south_map.items():
        situation_map[y2][x2] = SOUTH
        situation_map[y1][x1] = EMPTY


def main():
    situation_map = get_situation_map()

    x_size = len(situation_map[0])
    y_size = len(situation_map)

    step = 0
    for step in count(1):
        move_east_map = {}
        move_east(situation_map, move_east_map, x_size, y_size)

        move_south_map = {}
        move_south(situation_map, move_south_map, x_size, y_size)

        if not move_east_map and not move_south_map:
            break

    print(step)


if __name__ == '__main__':
    main()
