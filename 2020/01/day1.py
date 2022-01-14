with open('input.txt') as file:
    nums = [int(num) for num in file]

cals = {}
for i, num in enumerate(nums):
    diff = 2020 - num
    if diff in cals:
        print(num * nums[cals[diff]])
        break
    cals[num] = i
