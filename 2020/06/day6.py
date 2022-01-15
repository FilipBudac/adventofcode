with open('input.txt') as file:
    answers = [map(set, group.splitlines()) for group in file.read().split('\n\n')]

print(sum(len(set.union(*answer)) for answer in answers))
