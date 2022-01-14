with open('input.txt') as file:
    nums = [int(num) for num in file]

cals = {}
for i, num in enumerate(nums):
    diff = 2020 - num
    for j, other_num in enumerate(nums[i + 1:]):
        other_diff = diff - other_num
        if other_diff in cals:
            print(num * other_num * nums[cals[other_diff]])
            break
        cals[num] = i
