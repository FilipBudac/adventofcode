import re


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


with open('input.txt') as file:
    sensors = sorted([[*map(int, re.findall(r"-?\d+", line))] for line in file])

for y in range(4_000_001):
    x = 0
    for sx, sy, bx, by in sensors:
        if dist(sx, sy, bx, by) >= dist(sx, sy, x, y):
            x = sx + dist(sx, sy, bx, by) - abs(sy - y) + 1
    if x <= 4_000_000:
        print(x * 4_000_000 + y)
        break
