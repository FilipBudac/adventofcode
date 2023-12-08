import itertools
import re


START, END = 'AAA', 'ZZZ'

with open('input.txt') as file:
    navs, nodes_data = file.read().split('\n\n')

nodes = {}
for src, l, r in [re.match(r'(\w{3}) = \((\w{3}), (\w{3})\)', line).groups() for line in nodes_data.splitlines()]:
    nodes[src] = (l, r)

node = nodes[START]
for i, nav in enumerate(itertools.cycle(navs), 1):
    l, r = node
    if nav == 'L':
        if l == END:
            break
        node = nodes[l]
    else:
        if r == END:
            break
        node = nodes[r]

print(i)
