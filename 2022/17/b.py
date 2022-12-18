with open('input.txt') as file:
    data = file.read().strip()


def get_piece(type, y):
    if type == 0:
        return {(2, y), (3, y), (4, y), (5, y)}
    elif type == 1:
        return {(3, y + 2), (2, y + 1), (3, y + 1), (4, y + 1), (3, y)}
    elif type == 2:
        return {(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)}
    elif type == 3:
        return {(2, y), (2, y + 1), (2, y + 2), (2, y + 3)}
    elif type == 4:
        return {(2, y + 1), (2, y), (3, y + 1), (3, y)}


def move_left(p):
    if any(x == 0 for (x, y) in p):
        return p
    return {(x - 1, y) for (x, y) in p}


def move_right(p):
    if any(x == 6 for (x, y) in p):
        return p
    return {(x + 1, y) for (x, y) in p}


def move_down(p):
    return {(x, y - 1) for (x, y) in p}


def move_up(p):
    return {(x, y + 1) for (x, y) in p}


def signature(r):
    max_y = max(y for (x, y) in r)
    return frozenset((x, max_y - y) for (x, y) in r if max_y - y <= 30)


rock = {(x, 0) for x in range(7)}
tall, cur, rocks, added = 0, 0, 0, 0
seen = {}
while rocks < 1_000_000_000_000:
    piece = get_piece(rocks % 5, tall + 4)
    while True:
        if data[cur] == '<':
            piece = move_left(piece)
            if piece & rock:
                piece = move_right(piece)
        if data[cur] == '>':
            piece = move_right(piece)
            if piece & rock:
                piece = move_left(piece)
        cur = (cur + 1) % len(data)
        piece = move_down(piece)

        if piece & rock:
            rock |= move_up(piece)
            tall = max(y for (x, y) in rock)
            s = (cur, rocks % 5, signature(rock))
            if s in seen:
                pt, py = seen[s]
                dy = tall - py
                dt = rocks - pt
                amt = (1_000_000_000_000 - rocks) // dt
                added += amt * dy
                rocks += amt * dt
            seen[s] = (rocks, tall)
            break
    rocks += 1

print(tall + added)
