import math


def direct(c):
    """ Returns the sign of c: -1 if c < 0, 0 if c == 0, 1 if c > 0 """
    return (c > 0) - (c < 0)


def move_tail(hx, hy, tx, ty):
    return math.hypot(hx - tx, hy - ty) >= 2


DIRECT = {
    'R': lambda x, y: (x + 1, y),
    'L': lambda x, y: (x - 1, y),
    'U': lambda x, y: (x, y + 1),
    'D': lambda x, y: (x, y - 1),
}

with open('input.txt') as file:
    lines = [(line.split()[0], int(line.split()[1])) for line in file]

seen = set()
head, tail = (0, 0), (0, 0)
for (d, steps) in lines:
    for _ in range(steps):
        hx, hy = head
        tx, ty = tail
        head = DIRECT[d](*head)
        if move_tail(*head, *tail):
            tail = tx + direct(hx - tx), ty + direct(hy - ty)
        seen.add(tail)

print(len(seen))
