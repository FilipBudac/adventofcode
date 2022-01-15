with open('input.txt') as file:
    answers = [''.join(group.splitlines()) for group in file.read().split('\n\n')]

print(sum([len(set(answer)) for answer in answers]))
