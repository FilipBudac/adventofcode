with open('input.txt') as f:
    l1, l2 = zip(*(map(int, line.split()) for line in f))


print(sum(v1 * l2.count(v1) for v1 in l1))
