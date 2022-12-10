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


for pos, reg in enumerate(signals):
    if pos % 40 == 0:
        print(end='\n')
    if pos % 40 in (reg - 1, reg, reg + 1):
        print('#', end='')
    else:
        print('.', end='')

