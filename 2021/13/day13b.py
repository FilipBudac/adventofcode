import re

COORD_X = 'x'
COORD_Y = 'y'


def get_dots_with_instructions():
    with open('input.txt') as f:
        dots = set()
        while line := f.readline().strip():
            dots.add(tuple(map(int, line.split(','))))

        instructions = []
        while instruction := f.readline().strip():
            if search := re.search(r'(x|y)=(\d+)', instruction):
                coord, num = search.groups()
                instructions.append((coord, int(num)))

    return dots, instructions


def fold(dots, instruction):
    coord, num = instruction
    if coord == COORD_X:
        flip_dots = {(x, y) for (x, y) in dots if x > num}
        new_dots = {(num - (x - num), y) for (x, y) in flip_dots}
    else:
        flip_dots = {(x, y) for (x, y) in dots if y > num}
        new_dots = {(x, num - (y - num)) for (x, y) in flip_dots}
    dots.difference_update(flip_dots)
    dots.update(new_dots)


def print_letters_from_dots(dots):
    max_x = max(x for x, _ in dots)
    max_y = max(y for _, y in dots)

    res = ''
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            res += '#' if (x, y) in dots else ' '
        res += '\n'

    print(res)


def main():
    dots, instructions = get_dots_with_instructions()
    for instruction in instructions:
        fold(dots, instruction)
    print_letters_from_dots(dots)


if __name__ == '__main__':
    main()
