import collections
import itertools
import re


with open('input.txt') as file:
    cargos, ins = file.read().split('\n\n')

state = collections.defaultdict(list)
for line in itertools.zip_longest(*cargos.splitlines()):
    num, *letters = reversed(line)
    if num and num.isnumeric():
        state[int(num)].extend([l for l in letters if l not in [' ', None]])

for (size, f, t) in [[*map(int, re.findall(r'\d+', i))] for i in ins.splitlines()]:
    state[t].extend(state[f][-size:])
    del state[f][-size:]

print(''.join(v[-1] for v in state.values()))
