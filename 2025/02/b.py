import textwrap

ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in open('input.txt').read().split(',')]

invalid = set()
for s, e in ranges:
    for m in range(s, e + 1):
        for i in range(len(str(m)) // 2):
            if len(set(textwrap.wrap(str(m), i + 1))) == 1:
                invalid.add(m)

print(sum(invalid))
