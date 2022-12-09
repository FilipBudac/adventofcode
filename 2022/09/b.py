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
rope = [(0, 0)] * 10
for (d, steps) in lines:
    for _ in range(steps):
        rope[0] = DIRECT[d](*rope[0])
        for i in range(len(rope) - 1):
            hx, hy = rope[i]
            tx, ty = rope[i + 1]
            if move_tail(*rope[i], *rope[i + 1]):
                rope[i + 1] = tx + direct(hx - tx), ty + direct(hy - ty)
        seen.add(rope[-1])

print(len(seen))
