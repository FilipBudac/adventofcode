with open('input.txt') as file:
    answers = [map(set, group.splitlines()) for group in file.read().split('\n\n')]

print(sum(len(set.intersection(*answer)) for answer in answers))
