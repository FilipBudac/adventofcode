with open('input.txt') as file:
    instruction_groups = [list(instructions.strip()) for instructions in file]


def calc_pos(instructions, direction, low, high):
    ins = instructions.pop(0)
    if ins == direction:
        diff = high - low
        low, high = (low, low + diff // 2)
    else:
        diff = high - low
        low, high = (low + round(diff / 2), high)

    if not instructions:
        return low if ins == direction else high

    return calc_pos(instructions, direction, low, high)


print(max(calc_pos(instructions[0:7], 'F', 0, 127) * 8 + calc_pos(instructions[7:], 'L', 0, 7) for instructions in instruction_groups))