import itertools
import operator


def join(a, b):
    return int(f'{a}{b}')


def resolve(equation):
    v, *nums = equation
    for ops in itertools.product((join, operator.add, operator.mul), repeat=len(nums) - 1):
        sum_ = nums[0]
        for num, op in zip(nums[1:], ops):
            sum_ = op(sum_, num)
        if sum_ == v:
            return v
    return 0


equations = [[*map(int, e.replace(':', '').split())] for e in open('input.txt')]

print(sum(resolve(e) for e in equations))



