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

    return dots


def main():
    dots, instructions = get_dots_with_instructions()
    print(len(fold(dots, instructions.pop(0))))


if __name__ == '__main__':
    main()
