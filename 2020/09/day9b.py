from collections import deque

PRE_AMBLE_LEN = 25


def find_invalid_num():
    for num in nums_sequence:
        if not any(num - p_num in preamble for p_num in preamble):
            return num
        preamble.append(num)


def find_contiguous_sequence():
    for i, num in enumerate(all_nums):
        sequence = [num]
        sequence_sum = 0
        j = i + 1
        while sequence_sum < invalid_num:
            sequence.append(all_nums[j])
            sequence_sum = sum(sequence)
            j += 1
        if sequence_sum == invalid_num:
            return max(sequence) + min(sequence)


with open('input.txt') as file:
    all_nums = [int(line) for line in file]


preamble = deque(all_nums[:PRE_AMBLE_LEN], PRE_AMBLE_LEN)
nums_sequence = all_nums[PRE_AMBLE_LEN:]

invalid_num = find_invalid_num()
contiguous_sequence = find_contiguous_sequence()
print(contiguous_sequence)

