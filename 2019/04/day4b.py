with open('input.txt') as file:
    start, end = list(map(int, file.read().split('-')))


def has_adjacent_pair(num):
    return any((num.index(digit) + 1 + num[::-1].index(digit) + 1) == len(num) for digit in num)


def has_increasing_digits(num):
    return all(other >= dig for dig, other in zip(num, num[1:]))


print(sum(has_adjacent_pair(str(num)) and has_increasing_digits(str(num)) for num in range(start, end + 1)))
