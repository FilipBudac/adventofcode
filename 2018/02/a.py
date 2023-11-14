import collections

with open('input.txt') as file:
    box_ids = list(map(str.rstrip, file.readlines()))

counted = list(map(collections.Counter, box_ids))

twos = sum(2 in c.values() for c in counted)
threes = sum(3 in c.values() for c in counted)

print(twos * threes)

