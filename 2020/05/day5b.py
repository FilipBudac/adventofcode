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


def my_id(ids):
    """
    my_id = total_sum - actual_sum, where
      total_sum -> n(n+1)/2 (since we are not starting from 1, we need to adjust an interval of ids n(n+1)/2 - n(n-1)/2)
      actual_sum -> sum(ids)
    """
    max_id = max(ids)
    min_id = min(ids)

    total_sum = (max_id * (max_id + 1) // 2) - (min_id * (min_id - 1) // 2)
    actual_sum = sum(ids)

    return total_sum - actual_sum


print(my_id([calc_pos(instructions[0:7], 'F', 0, 127) * 8 + calc_pos(instructions[7:], 'L', 0, 7) for instructions in instruction_groups]))

