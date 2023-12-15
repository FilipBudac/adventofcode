def count(records, groups):
    if not groups:
        return 0 if records.count("#") else 1
    size = groups[0]

    tot, d = 0, 0
    s_max = len(records)
    for i, ch in enumerate(records):
        if (i - size + 1) > s_max:
            break

        if ch == '#' and s_max == len(records):
            s_max = i

        if ch in '#?':
            d = min(d + 1, size)
        else:
            d = 0

        n_ch = '.' if i + 1 == len(records) else records[i + 1]
        if d == size and n_ch in '.?':
            tot += count(records[i + 2:], groups[1:])

    return tot


with open('input.txt') as file:
    lines = []
    for line in file:
        records, groups = line.split()
        lines.append((records, [*map(int, groups.split(','))]))

print(sum(count(records, groups) for records, groups in lines))