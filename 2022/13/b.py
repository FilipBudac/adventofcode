import functools


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
    lines = [*map(eval, file.read().replace('\n\n', '\n').splitlines())] + [[[2]], [[6]]]

lines = sorted(lines, key=functools.cmp_to_key(cmp))

f_div = lines.index([[2]]) + 1
s_div = lines.index([[6]], f_div) + 1
print(f_div * s_div)
