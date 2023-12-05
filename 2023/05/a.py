import collections
import re


def get_location_for_seed(seed):
    for kind in transfers:
        for dest, src, len_ in transfers[kind]:
            if src <= seed <= (src + len_):
                seed += dest - src
                break
    return seed


with open('input.txt') as file:
    seeds_data, *almanac = file.read().split('\n\n')

transfers = collections.defaultdict(list)
for map_ in almanac:
    ins, *nums_data = map_.split('\n')
    k = re.match(r'(\w+)-to-(\w+)', ins).group(0)
    for nums in nums_data:
        transfers[k].append([*map(int, nums.split())])

seeds = map(int, re.findall(r'\d+', seeds_data))

print(min(get_location_for_seed(seed) for seed in seeds))