import collections
import itertools

with open('input.txt') as file:
    lines = map(str.rstrip, file.read().splitlines())

dirs_size = collections.defaultdict(int)
dirs = []
for l in lines:
    if l.endswith('ls') or l.startswith('dir'):
        continue
    a, *parts = l.split()
    if a.isnumeric():
        file, = parts
        for p in itertools.accumulate(dirs, func=lambda d, n: d + '/' + n):
            dirs_size[p] += int(a)
    else:
        _, dest = parts
        dirs.pop() if dest == '..' else dirs.append(dest)


print(min(t for t in dirs_size.values() if t >= dirs_size['/'] - 40000000))
