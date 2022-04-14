UP, DOWN, LEFT, RIGHT = 'UDLR'


def format_inp(inp):
    return inp[:1], int(inp[1:])


def move_wire(wire):
    grid = set()
    x, y = 0, 0
    for (direc, val) in wire:
        for _ in range(val):
            if direc in (LEFT, RIGHT):
                x += 1 if direc == RIGHT else -1
            if direc in (UP, DOWN):
                y += 1 if direc == DOWN else -1
            grid.add((x, y))

    return grid


with open('input3.txt') as file:
    wire_1, wire_2 = map(format_inp, file.readline().split(',')), map(format_inp, file.readline().split(','))

points_1, points_2 = move_wire(wire_1), move_wire(wire_2)

crossed_points = points_1.intersection(points_2)

print(min(abs(x) + abs(y) for (x, y) in crossed_points))
