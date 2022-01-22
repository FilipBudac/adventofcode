from collections import deque

PRE_AMBLE_LEN = 25


def find_invalid_num():
    for num in nums_sequence:
        if not any(num - p_num in preamble for p_num in preamble):
            return num
        preamble.append(num)


with open('input.txt') as file:
    all_nums = [int(line) for line in file]


preamble = deque(all_nums[:PRE_AMBLE_LEN], PRE_AMBLE_LEN)
nums_sequence = all_nums[PRE_AMBLE_LEN:]

invalid_num = find_invalid_num()
print(invalid_num)
