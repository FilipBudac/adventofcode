def move_sand(x, y):
    if y == floor:
        return x, y, -1
    if (x, y + 1) not in blocks:
        return x, y + 1, 1
    if (x - 1, y + 1) not in blocks:
        return x - 1, y + 1, 1
    if (x + 1, y + 1) not in blocks:
        return x + 1, y + 1, 1
    return x, y, 0


with open('input.txt') as file:
    lines = [[[*map(int, rock.split(','))] for rock in line.split(' -> ')] for line in file]

blocks = set()
for l in lines:
    for (x1, y1), (x2, y2) in zip(l, l[1:]):
        if x1 == x2:
            blocks |= set((x1, y) for y in range(min(y1, y2), max(y1, y2) + 1))
        if y1 == y2:
            blocks |= set((x, y1) for x in range(min(x1, x2), max(x1, x2) + 1))
floor = max(y for x, y in blocks)

tot = 0
while True:
    x, y = (500, 0)
    while True:
        x, y, moved = move_sand(x, y)
        if moved < 1:
            break
    if moved < 0:
        break
    blocks.add((x, y))
    tot += 1

print(tot)
