import re

monkeys = []
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

for _ in range(20):
    for m in monkeys:
        for old in m['items']:
            m['qty'] += 1
            op = eval(m['op'])
            level = op // 3
            if level % m['test'] == 0:
                monkeys[m['true']]['items'].append(level)
            else:
                monkeys[m['false']]['items'].append(level)
        m['items'] = []

a, b = sorted(m['qty'] for m in monkeys)[-2:]
print(a * b)
