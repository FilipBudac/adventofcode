import re

DELTAS = ((1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1))


def has_neighbour(y1, y2, specials):
    return any((x + dx, ny + dy) in specials for ny in range(y1, y2) for dx, dy in DELTAS)


with open('input.txt') as file:
    lines = list(map(str.rstrip, file.readlines()))

parts = []
for x, line in enumerate(lines):
    nums = {(m.start(), m.end()): int(m.group()) for m in re.finditer(r'\d+', line)}

    specials = {(x, m.end() - 1): m.group() for m in re.finditer(r'[^\w\s.]', line)}
    if x > 0:
        specials |= {(x - 1, m.end() - 1): m.group() for m in re.finditer(r'[^\w\s.]', lines[x - 1])}
    if x < len(lines[0]) - 1:
        specials |= {(x + 1, m.end() - 1): m.group() for m in re.finditer(r'[^\w\s.]', lines[x + 1])}

    for (y1, y2), num in nums.items():
        if has_neighbour(y1, y2, specials):
            parts.append(num)

print(sum(parts))

