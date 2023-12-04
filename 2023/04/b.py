import collections
import re


with open('input.txt') as file:
    data = list(map(lambda line: re.match(r'^Card\s+(\d+):\s+([\d\s]+)\s+\|\s+([\d\s]+)$', line).groups(), file.readlines()))


copies = collections.defaultdict(int)
for id_, w_nums, nums in data:
    copies[int(id_)] += 1
    for i in range(len(set(nums.split()) & set(w_nums.split()))):
        copies[int(id_) + i + 1] += copies[int(id_)]

print(sum(copies.values()))
