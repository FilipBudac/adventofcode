with open('input.txt') as file:
    lines = file.read().strip()


def get_piece(t, y):
    if t == 0:
        return {(2, y), (3, y), (4, y), (5, y)}
    elif t == 1:
        return {(3, y + 2), (2, y + 1), (3, y + 1), (4, y + 1), (3, y)}
    elif t == 2:
        return {(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)}
    elif t == 3:
        return {(2, y), (2, y + 1), (2, y + 2), (2, y + 3)}
    elif t == 4:
        return {(2, y + 1), (2, y), (3, y + 1), (3, y)}


def move_left(p):
    if any(x == 0 for x, y in p):
        return p
    return {(x - 1, y) for x, y in p}


def move_right(p):
    if any(x == 6 for x, y in p):
        return p
    return {(x + 1, y) for x, y in p}


def move_down(p):
    return {(x, y - 1) for x, y in p}


def move_up(p):
    return {(x, y + 1) for x, y in p}


rock = {(x, 0) for x in range(7)}
top, cur, rocks = 0, 0, 0
while rocks < 2022:
    piece = get_piece(rocks % 5, top + 4)
    while True:
        if lines[cur] == '<':
            piece = move_left(piece)
            if piece & rock:
                piece = move_right(piece)
        if lines[cur] == '>':
            piece = move_right(piece)
            if piece & rock:
                piece = move_left(piece)
        cur = (cur + 1) % len(lines)
        piece = move_down(piece)

        if piece & rock:
            rock |= move_up(piece)
            top = max(y for (x, y) in rock)
            break
    rocks += 1

print(top)
