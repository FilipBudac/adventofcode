with open('input.txt') as file:
    instructions = [list(ins.strip()) for ins in file]


def calc_pos(instructions, dir, low, high):
    ins = instructions.pop(0)
    if ins == dir:
        diff = abs(low - high)
        low, high = (low, low + diff // 2)
    else:
        diff = abs(low - high)
        low, high = (low + round(diff / 2), high)

    if not instructions:
        return low if ins == dir else high

    return calc_pos(instructions, dir, low, high)


print(max(calc_pos(ins[0:7], 'F', 0, 127) * 8 + calc_pos(ins[7:], 'L', 0, 7) for ins in instructions))
