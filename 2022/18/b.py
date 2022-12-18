def neighbors(x, y, z):
    return (x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)


def droplets(queue):
    seen = set()
    while queue:
        cur = queue.pop(0)
        if cur in seen:
            continue
        if min(cur) < min(min(c) for c in cubes) or max(cur) > max(max(c) for c in cubes):
            return set()
        for n in neighbors(*cur):
            if n not in queue and n not in cubes:
                queue.append(n)
        seen.add(cur)
    return seen


with open('input.txt') as file:
    cubes = [tuple(map(int, l.rstrip().split(','))) for l in file]

d = set()
surface = 0
for c in cubes:
    for n in neighbors(*c):
        if n in cubes or n in d:
            continue
        if nd := droplets([n]):
            d.update(nd)
            continue
        surface += 1

print(surface)
