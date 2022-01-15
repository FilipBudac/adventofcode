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


ids = [calc_pos(ins[0:7], 'F', 0, 127) * 8 + calc_pos(ins[7:], 'L', 0, 7) for ins in instructions]
max_id = max(ids)
min_id = min(ids)

# total_sum - actual_sum
# total_sum -> n(n+1)/2
# actual_sum -> sum(ids)
# we are not starting from 1, so we need to adjust an interval of ids
# n(n+1)/2 - n(n-1)/2
total_sum = (max_id * (max_id + 1) // 2) - (min_id * (min_id - 1) // 2)
actual_sum = sum(ids)
my_id = total_sum - actual_sum

print(my_id)
