from functools import lru_cache


@lru_cache()
def arrangements(cur):
    if cur == len(nums) - 1:
        return 1

    count = 0
    for other in range(cur + 1, min(cur + 4, len(nums))):
        if nums[other] - nums[cur] > 3:
            continue
        count += arrangements(other)

    return count


with open('input.txt') as file:
    nums = [int(num) for num in file]

nums = [0] + nums + [max(nums) + 3]
nums = sorted(nums)

print(arrangements(0))
