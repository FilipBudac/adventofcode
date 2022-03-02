with open('input.txt') as file:
    nums = [int(num) for num in file]

nums = [0] + nums + [max(nums) + 3]
nums = sorted(nums)

diff_three = diff_one = 0
for num, other in zip(nums, nums[1:]):
    delta = other - num
    if delta == 1:
        diff_one += 1
    if delta == 3:
        diff_three += 1


print(diff_one * diff_three)