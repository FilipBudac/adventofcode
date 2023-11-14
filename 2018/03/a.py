import collections
import re

with open('input.txt') as file:
    data = [list(map(int, re.match(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)', line).groups())) for line in file]


grid = collections.defaultdict(int)
for id_, from_left, from_top, width, height in data:
    for x in range(height):
        for y in range(width):
            grid[(from_left + y + 1, from_top + x + 1)] += 1

print(sum(v > 1 for v in grid.values()))