import collections
import functools
import operator
import re

DELTAS = ((1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1))


def get_neighbours(specials, x, y1, y2):
    return ((x + dx, ny + dy) for ny in range(y1, y2) for dx, dy in DELTAS if (x + dx, ny + dy) in specials)


with open('input.txt') as file:
    lines = list(map(str.rstrip, file.readlines()))

adjs = collections.defaultdict(list)
for x, line in enumerate(lines):
    nums = {(m.start(), m.end()): int(m.group()) for m in re.finditer(r'\d+', line)}

    specials = {(x, m.end() - 1): m.group() for m in re.finditer(r'[^\w\s.]', line)}
    if x > 0:
        specials |= {(x - 1, m.end() - 1): m.group() for m in re.finditer(r'[^\w\s.]', lines[x - 1])}
    if x < len(lines[0]) - 1:
        specials |= {(x + 1, m.end() - 1): m.group() for m in re.finditer(r'[^\w\s.]', lines[x + 1])}

    for (y1, y2), num in nums.items():
        for sx, sy in get_neighbours(specials, x, y1, y2):
            if num not in adjs[sx, sy]:
                adjs[sx, sy].append(num)

print(sum(functools.reduce(operator.mul, nums) for nums in adjs.values() if len(nums) == 2))

