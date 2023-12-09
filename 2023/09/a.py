def extrapolate(h):
    cur = h[0][-1]
    for i, _ in enumerate(h[:-1], 1):
        l = h[i][-1]
        cur = l + cur

    return cur

def generate(hists):
    hists.append([b - a for a, b in zip(hists[-1], hists[-1][1:])])

    if any(hists[-1]):
        return generate(hists)

    return [*reversed(hists)]

with open('input.txt') as file:
    histories = [[*map(int, line.split())] for line in file]

print(sum(extrapolate(generate([h])) for h in histories))
