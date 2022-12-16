import re
import itertools

with open('input.txt') as file:
    lines = file.readlines()


valves, flows = {}, {}
for l in lines:
    v, *tunnels = re.findall(r'[A-Z]{2}', l)
    flows[v] = int(re.search(r'\d+', l).group())
    valves[v] = tunnels


d = {}
for f, t in itertools.combinations([v for v, f in flows.items() if f > 0] + ['AA'], 2):
    seen = {f: 0}
    q = [(f, 0)]
    while q:
        cur, dist = q.pop(0)
        for dest in valves[cur]:
            if dest in seen:
                continue
            q.append((dest, dist + 1))
            seen[dest] = dist + 1
        if t in seen:
            break
    d[tuple(sorted((f, t)))] = seen[t]


seen = {}
valves = [v for v, f in flows.items() if f > 0]
q = [('AA', [], 0, 26)]
while q:
    cur, op, p, t = q.pop(0)

    for dest in [v for v in valves if v not in op]:
        dist = d[tuple(sorted((cur, dest)))]
        nt = t - dist - 1
        if nt < 0:
            continue

        np = p + flows[dest] * nt
        nop = sorted([o for o in op] + [dest])

        if (dest, tuple(nop)) in seen and seen[dest, tuple(nop)] > np:
            continue

        seen[dest, tuple(nop)] = np
        q.append((dest, nop, np, nt))

valves = {}
for (_, op), p in seen.items():
    if op in valves and p < valves[op]:
        continue
    valves[op] = p

m = 0
for (o1, p1), (o2, p2) in itertools.product(valves.items(), valves.items()):
    if set(o1) & set(o2):
        continue
    m = max(p1 + p2, m)

print(m)
