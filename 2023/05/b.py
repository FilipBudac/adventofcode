import collections
import itertools
import re


def get_seed_for_location(transfers, location):
    for kind in transfers:
        for dest, src, len_ in transfers[kind]:
            if dest <= location <= (dest + len_):
                location += src - dest
                break
    return location


def find_location(transfers, seeds):
    for location in itertools.count():
        seed = get_seed_for_location(transfers, location)

        for f, t in seeds:
            if f <= seed <= (f + t):
                return location


with open('input.txt') as file:
    seeds_data, *almanac = file.read().split('\n\n')


transfers = collections.defaultdict(list)
for map_ in reversed(almanac):
    ins, *nums_data = map_.split('\n')
    k = re.match(r'(\w+)-to-(\w+)', ins).group(0)
    for nums in nums_data:
        transfers[k].append([*map(int, nums.split())])

seeds = [*map(int, re.findall(r'\d+', seeds_data))]
seeds = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]

print(find_location(transfers, seeds))