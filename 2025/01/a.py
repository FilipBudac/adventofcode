rotations = list(map(str.strip, open('input.txt').readlines()))

cur = 50
tot = 0
for r in rotations:
    dir_, val = r[0], int(r[1:])
    if dir_ == 'R':
        cur = (cur + val) % 100
    else:
        cur = (cur - val) % 100

    if cur == 0:
        tot += 1

print(tot)
