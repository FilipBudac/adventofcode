ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in open('input.txt').read().split(',')]

invalid = set()
for s, e in ranges:
    for m in range(s, e + 1):
        len_ = len(str(m)) // 2
        if str(m)[:len_] == str(m)[len_:]:
            invalid.add(m)

print(sum(invalid))

