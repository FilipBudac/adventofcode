lines = open('input.txt').read().split('\n\n')
fresh_ids = [list(map(int, l.split('-'))) for l in lines[0].split('\n')]
available_ids = [int(l) for l in lines[1].split('\n')]

tot = 0
for id_ in available_ids:
    for s, e in fresh_ids:
        if s <= id_ <= e:
            tot += 1
            break

print(tot)
