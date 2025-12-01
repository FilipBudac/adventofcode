rotations = list(map(str.strip, open('input.txt').readlines()))

cur = 50
tot = 0
for r in rotations:
    dir_, val = r[0], int(r[1:])
    for i in range(val):
        if dir_ == 'R':
            cur += 1
        else:
            cur -= 1
        cur = cur % 100
        if cur == 0:
            tot += 1

print(tot)
