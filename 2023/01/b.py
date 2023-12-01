import collections

DIGITS = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def check_for_digit(char, line):
    if char.isnumeric():
        return char
    for d in DIGITS:
        if d in line:
            return DIGITS[d]


with open('input.txt') as file:
    lines = map(str.rstrip, file.readlines())

pairs = collections.defaultdict(list)
for idx, line in enumerate(lines):

    for n, char in enumerate(line, 1):
        if digit := check_for_digit(char, line[:n]):
            pairs[idx].append(digit)
            break

    for n, char in enumerate(line[::-1], 1):
        if digit := check_for_digit(char, line[-n:]):
            pairs[idx].append(digit)
            break

print(sum(int(num[0] + num[-1]) for num in pairs.values()))
