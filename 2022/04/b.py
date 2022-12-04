with open('input.txt') as file:
    lines = [line.split(',') for line in file]
    sects = [[map(int, a.split('-')), map(int, b.split('-'))] for (a, b) in lines]

print(sum(min(e1, e2) >= max(s1, s2) for ((s1, e1), (s2, e2)) in sects))
