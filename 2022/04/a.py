with open('input.txt') as file:
    lines = [line.split(',') for line in file]
    sects = [[map(int, a.split('-')), map(int, b.split('-'))] for (a, b) in lines]

tot = 0
for ((s1, e1), (s2, e2)) in sects:
    if (s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1):
        tot += 1
print(tot)
