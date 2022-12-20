import operator
import re
import functools


def build(oc, cc, ooc, occ, goc, gobc, t):
    stack = [(0, 1, 0, 0, 0, 0, 0, 0, t)]
    seen = set()
    m = 0
    req = max(oc, cc, ooc, goc)
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)

        o, ro, c, rc, ob, rob, g, rg, t = cur
        ro = min(ro, req)
        no, nc, nob, ng = o + ro, c + rc, ob + rob, g + rg
        t -= 1
        if t == 0:
            m = max(m, ng)
            continue

        ext = False
        if o >= goc and ob >= gobc:
            stack.append((no - goc, ro, nc, rc, nob - gobc, rob, ng, rg + 1, t))
            ext = True
        if o >= ooc and c >= occ:
            stack.append((no - ooc, ro, nc - occ, rc, nob, rob + 1, ng, rg, t))
            ext = True
        if o >= cc:
            stack.append((no - cc, ro, nc, rc + 1, nob, rob, ng, rg, t))
            ext = True
        if o >= oc:
            stack.append((no - oc, ro + 1, nc, rc, nob, rob, ng, rg, t))
            ext = True

        if not ext:
            stack.append((no, ro, nc, rc, nob, rob, ng, rg, t))

    return m


with open('input.txt') as file:
    bp = [[*map(int, re.findall(r'\d+', l))] for l in file]

print(functools.reduce(operator.mul, [build(*nums, 32) for _, *nums in bp[:3]]))
