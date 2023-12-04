import re


with open('input.txt') as file:
    data = list(map(lambda line: re.match(r'^Card\s+(\d+):\s+([\d\s]+)\s+\|\s+([\d\s]+)$', line).groups(), file.readlines()))


matched = [len(set(nums.split()) & set(w_nums.split())) for id_, w_nums, nums in data]
print(sum(pow(2, m - 1) for m in matched if m))
