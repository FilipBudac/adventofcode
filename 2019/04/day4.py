with open('input.txt') as file:
    start, end = list(map(int, file.read().split('-')))


def has_adjacent_pair(num):
    return any(first == other for first, other in zip(num, num[1:]))


def has_increasing_digits(num):
    return all(other >= first for first, other in zip(num, num[1:]))


print(sum(has_adjacent_pair(str(num)) and has_increasing_digits(str(num)) for num in range(start, end + 1)))
