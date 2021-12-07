from collections import defaultdict


def get_initial_positions():
    with open('input.txt') as f:
        initial_positions = list(map(int, f.readline().split(',')))

    return initial_positions


def a(initial_positions):
    position_to_steps = defaultdict(int)
    for position in range(max(initial_positions)):
        for num in initial_positions:
            cost = abs(num - position)
            position_to_steps[position] += cost

    print(min(position_to_steps.values()))


def b(initial_positions):
    position_to_steps = defaultdict(int)
    for position in range(max(initial_positions)):
        for num in initial_positions:
            cost = sum(i for i in range(1, abs(num - position) + 1))
            position_to_steps[position] += cost

    print(min(position_to_steps.values()))


def main():
    numbers = get_initial_positions()
    a(numbers)
    b(numbers)


if __name__ == '__main__':
    main()
