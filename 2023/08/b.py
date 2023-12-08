import itertools
import math
import re


START, END = 'A', 'Z'

with open('input.txt') as file:
    navs, nodes_data = file.read().split('\n\n')

nodes = {}
for src, l, r in [re.match(r'(\w{3}) = \((\w{3}), (\w{3})\)', line).groups() for line in nodes_data.splitlines()]:
    nodes[src] = (l, r)

finishes = []
for src, node in {src: node for src, node in nodes.items() if src.endswith(START)}.items():
    for i, nav in enumerate(itertools.cycle(navs), 1):
        l, r = node

        if nav == 'L':
            if l.endswith(END):
                finishes.append(i)
                break
            node = nodes[l]

        else:
            if r.endswith(END):
                finishes.append(i)
                break
            node = nodes[r]

print(math.lcm(*finishes))
