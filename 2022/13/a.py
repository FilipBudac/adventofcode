def cmp(l, r):
    l_type, r_type = type(l), type(r)
    if l_type is int and r_type is int:
        return l - r

    if l_type is int or r_type is int:
        return cmp([l], r) if l_type is int else cmp(l, [r])

    for n, o in zip(l, r):
        if (res := cmp(n, o)) != 0:
            return res

    return len(l) - len(r)


with open('input.txt') as file:
    lines = [*map(str.splitlines, file.read().split('\n\n'))]

tot = 0
for pair, (l, r) in enumerate(lines, 1):
    l, r = eval(l), eval(r)
    if cmp(l, r) < 0:
        tot += pair

print(tot)
