import collections
import functools
import re
import operator


with open('input.txt') as file:
    times = [*map(int, re.findall(r'\d+', file.readline()))]
    distances = [*map(int, re.findall(r'\d+', file.readline()))]

races = collections.defaultdict(list)
for time, distance in zip(times, distances):
    for hold in range(time):
        race = (time - hold) * hold
        if race > distance:
            races[distance].append(race)

print(functools.reduce(operator.mul, [*map(len, races.values())]))
