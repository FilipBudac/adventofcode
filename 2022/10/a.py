import re

with open('input.txt') as file:
    lines = [re.match(r'(noop|addx)\s(-*\d+)*', line).groups() for line in file]

reg = 1
signals = [reg]
for (ins, val) in lines:
    signals.append(reg)
    if ins == 'addx':
        reg += int(val)
        signals.append(reg)


print(sum(signals[m - 1] * m for m in [20, 60, 100, 140, 180, 220]))
