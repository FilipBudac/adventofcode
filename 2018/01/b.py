import itertools


def find_2nd_occurrence(nums):
    tot = 0
    seen = set()
    for num in itertools.cycle(nums):
        tot += num

        if tot in seen:
            return tot

        seen.add(tot)


with open('input.txt') as file:
    nums = map(int, file.readlines())

print(find_2nd_occurrence(list(nums)))


