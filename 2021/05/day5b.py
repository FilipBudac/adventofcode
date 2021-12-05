from collections import defaultdict


def get_line_segments():
    with open('input.txt') as f:
        points = [row.split(' -> ') for row in f.readlines()]
        lines = [[point[0].strip().split(','), point[1].strip().split(',')] for point in points]

    return lines


def create_diagram(lines):
    diagram = defaultdict(int)
    for line in lines:
        (x1, y1), (x2, y2) = list([list(map(int, point)) for point in line])

        if x1 == x2:
            steps = abs(y1 - y2) + 1
            y = max(y1, y2)
            for i in range(steps):
                diagram[x1, y - i] += 1

        elif y1 == y2:
            steps = abs(x1 - x2) + 1
            x = max(x1, x2)
            for i in range(steps):
                diagram[x - i, y1] += 1

        else:
            if x1 < x2 and y1 < y2:
                x_steps = range(x1, x2 + 1)
                y_steps = range(y1, y2 + 1)
            elif x1 > x2 and y1 < y2:
                x_steps = range(x1, x2 - 1, -1)
                y_steps = range(y1, y2 + 1)
            elif x1 < x2 and y1 > y2:
                x_steps = range(x1, x2 + 1)
                y_steps = range(y1, y2 - 1, -1)
            else:
                x_steps = range(x1, x2 - 1, -1)
                y_steps = range(y1, y2 - 1, -1)

            for x, y in zip(x_steps, y_steps):
                diagram[x, y] += 1

    return diagram


def calc_result(diagram):
    return sum(val > 1 for val in diagram.values())


def main():
    lines = get_line_segments()
    diagram = create_diagram(lines)
    print(calc_result(diagram))


if __name__ == '__main__':
    main()