banks = list(map(str.strip, open('input.txt').readlines()))

output = 0
for b in banks:
    cur, idx = '', 0
    for i in reversed(range(0, 12)):
        end = None if i == 0 else -i
        max_ = str(max(map(int, b[idx:end])))

        cur += max_
        idx += b[idx:].index(max_) + 1

    output += int(cur)

print(output)
