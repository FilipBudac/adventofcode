import re


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


with open('input.txt') as file:
    sensors = [[*map(int, re.findall(r"-?\d+", line))] for line in file]

tot, y = 0, 2_000_000
for x in range(-1_000_000, 6_000_000):
    for sx, sy, bx, by in sensors:
        if dist(sx, sy, bx, by) >= dist(sx, sy, x, y) and (bx != x or by != y):
            tot += 1
            break
print(tot)
