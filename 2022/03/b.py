with open('input.txt') as file:
    rucks = [*map(str.rstrip, file)]

tot = 0
for r in range(0, len(rucks), 3):
    groups = map(set, rucks[r:r + 3])
    badge = set.intersection(*groups).pop()
    if badge.islower():
        tot += ord(badge) - ord('a') + 1
    else:
        tot += ord(badge) - ord('A') + 26 + 1
print(tot)
