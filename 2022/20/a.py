def middle(nums):
    return [i for i, (_, num) in enumerate(nums) if num == 0].pop()


def mix(file, nums):
    size = len(nums)
    for (i, num) in file:
        idx = nums.index((i, num))
        nums.pop(idx)
        idx = (idx + num) % (size - 1)
        nums.insert(idx, (i, num))
    return sum(nums[(middle(nums) + num) % size][1] for num in [1000, 2000, 3000])


with open('input.txt') as file:
    nums = [(i, int(l)) for i, l in enumerate(file)]

print(mix(nums, nums.copy()))
