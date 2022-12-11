import math
import re

monkeys, nums = [], []
with open('input.txt') as file:
    for (_, items, op, test, true, false) in map(str.splitlines, file.read().split('\n\n')):
        monkeys.append({
                'op': op.split(' = ')[-1],
                'items': [*map(int, re.findall(r'\d+', items))],
                'test': int(re.search(r'\d+', test).group()),
                'true': int(re.search(r'\d+', true).group()),
                'false': int(re.search(r'\d+', false).group()),
                'qty': 0
        })
        for old in monkeys[-1]['items']:
            nums.append(eval(monkeys[-1]['op']))

mod = math.lcm(*nums)
for _ in range(10_000):
    for m in monkeys:
        for old in m['items']:
            m['qty'] += 1
            op = eval(m['op'])
            level = op % mod
            if level % m['test'] == 0:
                monkeys[m['true']]['items'].append(level)
            else:
                monkeys[m['false']]['items'].append(level)
        m['items'] = []

a, b = sorted(m['qty'] for m in monkeys)[-2:]
print(a * b)
