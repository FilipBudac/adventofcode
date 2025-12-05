lines = open('input.txt').read().split('\n\n')
ids = [list(map(int, l.split('-'))) for l in lines[0].split('\n')]
ids.sort()

fresh = [ids[0]]
for s, e in ids[1:]:
    ps, pe = fresh[-1]
    if pe >= s:
        fresh[-1] = (ps, max(pe, e))
    else:
        fresh.append((s, e))

print(sum(e - s + 1 for s, e in fresh))



