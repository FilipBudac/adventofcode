import itertools


def find_similar_ids(box_ids):
    for id_, other in itertools.product(box_ids, box_ids[1:]):
        similar = ''.join(a for a, b in zip(id_, other) if a == b)
        if len(id_) == len(similar) + 1:
            return similar

with open('input.txt') as file:
    box_ids = list(map(str.rstrip, file.readlines()))

print(find_similar_ids(box_ids))
