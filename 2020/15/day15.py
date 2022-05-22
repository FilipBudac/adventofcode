LAST_TURN = 2020

with open('input.txt') as file:
    nums = list(map(int, file.readline().split(',')))

spoken = {num: i + 1 for i, num in enumerate(nums)}
last = nums[-1]
for turn in range(len(nums), LAST_TURN):
    next_turn = turn - spoken[last] if last in spoken else 0
    spoken[last] = turn
    last = next_turn

print(last)
