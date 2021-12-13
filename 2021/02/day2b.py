FORWARD = 'forward'
DOWN = 'down'
UP = 'up'


def get_instructions():
    with open('input.txt') as f:
        instructions = [(instruction, int(val)) for instruction, val in [line.split() for line in f.readlines()]]
    return instructions


def main():
    instructions = get_instructions()

    depth = horizontal = aim = 0
    for instruction, val in instructions:
        if instruction == DOWN:
            aim += val
        if instruction == UP:
            aim -= val
        if instruction == FORWARD:
            horizontal += val
            depth += aim * val

    print(depth * horizontal)


if __name__ == '__main__':
    main()
