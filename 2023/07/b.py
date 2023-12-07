import collections
import functools


JOKER = 'J'


def get_hand_scores(ordering, hand):
    cards, _ = hand
    score = [ordering.index(card) for card in cards]

    cards = collections.Counter(cards)

    if JOKER in cards:
        jokers = cards.get(JOKER)
        cards[JOKER] = 0

        card, _ = cards.most_common(1).pop()
        cards[card] += jokers

    scores = []
    match [n for n in cards.values() if n > 1]:
        case [5]:
            scores.extend([7] + score)
        case [4]:
            scores.extend([6] + score)
        case [2, 3] | [3, 2]:
            scores.extend([5] + score)
        case [3]:
            scores.extend([4] + score)
        case [2, 2]:
            scores.extend([3] + score)
        case [2]:
            scores.extend([2] + score)
        case []:
            scores.extend([1] + score)
    return scores


with open('input.txt') as file:
    hands = [l.split() for l in file]

hands = sorted(hands, key=functools.partial(get_hand_scores, "J123456789TQKA"))
print(sum(i * int(bid) for i, (_, bid) in enumerate(hands, 1)))
