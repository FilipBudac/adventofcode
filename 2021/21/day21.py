import re
from itertools import cycle

MAX_SCORE = 1000
THROWS = 3
STEPS = 100


def get_players():
    with open("input.txt") as f:
        players = [int(re.match(r'.+:\s(\d+)', line).groups()[0]) - 1 for line in f.readlines()]
    return players


def dirac_dice(die, player_1, player_2, score_1, score_2, throws):
    if score_2 >= MAX_SCORE:
        return score_1 * throws

    player_1 += sum(next(die) for _ in range(THROWS))
    player_1 = player_1 % 10

    score_1 += player_1 + 1

    return dirac_dice(die, player_2, player_1, score_2, score_1, throws + THROWS)


def main():
    print(dirac_dice(cycle(range(1, STEPS + 1)), *get_players(), 0, 0, 0))


if __name__ == '__main__':
    main()
