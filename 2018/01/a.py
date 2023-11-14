with open('input.txt') as file:
    nums = map(int, file.readlines())

print(sum(nums))
