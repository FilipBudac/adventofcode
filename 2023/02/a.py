import collections
import re


RGB_LIMITS = {'red': 12, 'green': 13, 'blue': 14}

with open('input.txt') as file:
    games = map(lambda game: re.match(r'Game\s(\d+):(.*)', game).groups(), file.readlines())

tot = 0
for game_id, turns in games:
    over = False
    for turn in turns.split(';'):
        rgb = collections.defaultdict(int)

        for qty, color in map(str.split, turn.split(',')):
            rgb[color] += int(qty)

        over |= any(int(qty) > RGB_LIMITS[c] for c, qty in rgb.items())

    if not over:
        tot += int(game_id)

print(tot)
