with open('input1.txt') as file:
    nums = list(map(int, file))

total = 0
for num in nums:
    while (num := num // 3 - 2) > 0:
        total += num

print(total)
