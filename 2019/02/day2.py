import operator

with open('input2.txt') as file:
    nums = list(map(int, file.read().split(',')))

ops = {1: operator.add, 2: operator.mul}

nums[1], nums[2] = 12, 2
for i in range(0, len(nums), 4):
    if nums[i] == 99:
        break
    p_1, p_2 = nums[nums[i + 1]], nums[nums[i + 2]]
    nums[nums[i + 3]] = ops[nums[i]](p_1, p_2)

print(nums[0])

