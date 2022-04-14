import operator


def run(nums, noun, verb):
    nums[1], nums[2] = noun, verb
    for i in range(0, len(nums), 4):
        if nums[i] == 99:
            break
        p_1, p_2 = nums[nums[i + 1]], nums[nums[i + 2]]
        nums[nums[i + 3]] = ops[nums[i]](p_1, p_2)
    return nums[0]


with open('input2.txt') as file:
    nums = list(map(int, file.read().split(',')))

ops = {1: operator.add, 2: operator.mul}

print(next(100 * noun + verb for noun in range(100) for verb in range(100) if run(nums[:], noun, verb) == 19690720))
