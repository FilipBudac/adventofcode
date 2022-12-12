import heapq

with open('input.txt') as file:
    heightmap = {(x, y): char for x, line in enumerate(file) for y, char in enumerate(line.rstrip())}

def neighbours(x, y):
    return [(x + dx, y + dy) for dx, dy in ((1, 0), (0, -1), (0, 1), (-1, 0))]


def find_best_signal(source, dest):
    cur = []
    seen = set()
    for coord, ch in heightmap.items():
        if ch in source:
            heapq.heappush(cur, (0, *coord))

    while cur:
        dist, x, y = heapq.heappop(cur)
        for (nx, ny) in neighbours(x, y):
            if (nx, ny) in seen or (nx, ny) not in heightmap:
                continue
            hs = heightmap[x, y] if heightmap[x, y] != source else 'a'
            hd = heightmap[nx, ny] if heightmap[nx, ny] != dest else 'z'
            if ord(hd) - ord(hs) > 1:
                continue
            if heightmap[nx, ny] == dest:
                return dist + 1
            heapq.heappush(cur, (dist + 1, nx, ny))
            seen.add((nx, ny))


print(find_best_signal(['a', 'S'], 'E'))
