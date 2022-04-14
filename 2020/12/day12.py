NORTH, SOUTH, EAST, WEST = 'NSEW'
LEFT, RIGHT = 'LR'

MOVE = {
    NORTH: lambda x, y, val: (x, y + val),
    SOUTH: lambda x, y, val: (x, y - val),
    EAST: lambda x, y, val: (x + val, y),
    WEST: lambda x, y, val: (x - val, y),
}

# (1, 0) EAST
# (-1, 0) WEST
# (0, 1) NORTH
# (0, -1) SOUTH

# (1, 0) left 90
# (0, 1) left 90
# (-1, 0) left 90
# (0, -1) left 90
# (1, 0) left 270
# (0, -1)

TURN = {
    (LEFT, 90): lambda x, y: (-y, x),
    (LEFT, 180): lambda x, y: (-x, -y),
    (LEFT, 270): lambda x, y: (y, -x),
    (RIGHT, 90): lambda x, y: (y, -x),
    (RIGHT, 180): lambda x, y: (-x, -y),
    (RIGHT, 270): lambda x, y: (-y, x),
}

with open('input.txt') as file:
    actions = list(map(lambda line: (line[0], int(line[1:])), file))

pos, direct = (0, 0), (1, 0)
for act, val in actions:
    if act in [NORTH, SOUTH, EAST, WEST]:
        pos = MOVE[act](*pos, val)
    elif act in [LEFT, RIGHT]:
        direct = TURN[act, val](*direct)
    else:
        x, y = pos
        d_x, d_y = direct
        pos = (x + d_x * val, y + d_y * val)

print(abs(pos[0]) + abs(pos[1]))
