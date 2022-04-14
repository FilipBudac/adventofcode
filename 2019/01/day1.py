with open('input1.txt') as file:
    nums = list(map(int, file))

print(sum(num // 3 - 2 for num in nums))
