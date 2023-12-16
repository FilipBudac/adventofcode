def reflections(mirror, ignore=-1):
    size = len(mirror)

    for i in range(size - 1):
        step = 0

        while i - step >= 0 and i + step + 1 < size:
            if mirror[i - step] != mirror[i + step + 1]:
                break
            step += 1
        else:
            if i + 1 == ignore:
                continue

            return i + 1

    return 0


with open('input.txt') as file:
    mirrors = file.read().split('\n\n')

tot = 0
for m in [m.splitlines() for m in mirrors]:
    i_row = reflections(m)
    i_col = reflections(list(zip(*m)))

    res = set()
    for i, row in enumerate(m):
        for j, ch in enumerate(row):
            new = '#' if ch == '.' else '.'

            m[i] = m[i][:j] + new + m[i][j + 1:]

            rows = reflections(m, ignore=i_row)
            cols = reflections(list(zip(*m)), ignore=i_col)

            res.add((rows, cols))

            m[i] = m[i][:j] + ch + m[i][j + 1:]

    rows, cols = res.pop()
    tot += rows * 100 + cols

print(tot)
