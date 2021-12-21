import re
from functools import lru_cache
from itertools import product

MAX_SCORE = 21
ROLLS = tuple(map(sum, product(range(1, 4), range(1, 4), range(1, 4))))


def get_players():
    with open("input.txt") as f:
        players = [int(re.match(r'.+:\s(\d+)', line).groups()[0]) - 1 for line in f.readlines()]
    return players


@lru_cache(maxsize=None)
def dirac_dice(player_1, player_2, score_1, score_2):
    if score_2 >= MAX_SCORE:
        return 0, 1

    wins = [0, 0]
    for roll in ROLLS:
        player = (player_1 + roll) % 10
        score = score_1 + player + 1

        win_2, win_1 = dirac_dice(player_2, player, score_2, score)

        wins[0] += win_1
        wins[1] += win_2

    return wins


def main():
    print(max(dirac_dice(*get_players(), 0, 0)))


if __name__ == '__main__':
    main()
