import collections
import re
import functools


with open('input.txt') as file:
    games = map(lambda game: re.match(r'Game\s(\d+):(.*)', game).groups(), file.readlines())

tot = 0
for game_id, turns in games:
    rgb_max = collections.defaultdict(int)
    for turn in turns.split(';'):
        rgb = collections.defaultdict(int)

        for qty, color in map(str.split, turn.split(',')):
            rgb[color] += int(qty)

        rgb_max = {color: max(rgb[color], rgb_max[color]) for color in {'red', 'green', 'blue'}}

    tot += functools.reduce((lambda x, y: x * y), rgb_max.values())

print(tot)
