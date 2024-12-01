with open('input.txt') as f:
    l1, l2 = zip(*(map(int, line.split()) for line in f))

print(sum(abs(v1 - v2) for v1, v2 in zip(sorted(l1), sorted(l2))))
