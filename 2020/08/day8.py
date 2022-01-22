def loop():
    c = acc = 0
    seen = set()
    while c not in seen:
        ins, val = instructions[c]
        seen.add(c)
        if ins == 'acc':
            acc += int(val)
        if ins == 'jmp':
            c += int(val) - 1
        c += 1
    return acc


with open('input.txt') as file:
    instructions = [tuple(line.strip().split(' ')) for line in file]

print(loop())
