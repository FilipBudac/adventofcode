from itertools import count

SQUARE_WIDTH = 3
SQUARE_HEIGHT = 3


def get_algorithm_with_image():
    with open('input.txt') as f:
        algorithm = None
        while line := f.readline().strip():
            algorithm = line
        image = [insertion.strip() for insertion in f.readlines()]
    return algorithm, image


def enhance(step, lights, algorithm):
    new_lights = set()

    min_x, max_x = min(x for x, y in lights), max(x for x, y in lights)
    min_y, max_y = min(y for x, y in lights), max(y for x, y in lights)

    for y in range(min_y - 2, max_y + 2):
        for x in range(min_x - 2, max_x + 2):
            binary_num = 0
            for square_y in range(SQUARE_WIDTH):
                for square_x in range(SQUARE_HEIGHT):
                    if (x + square_x, y + square_y) in lights:
                        binary_num += pow(2, (2 - square_y) * 3 + (2 - square_x))
                    elif algorithm[0] == "#" and step % 2 == 0:
                        if (x + square_x) < min_x or (x + square_x) > max_x:
                            binary_num += pow(2, (2 - square_y) * 3 + (2 - square_x))
                        elif (y + square_y) < min_y or (y + square_y) > max_y:
                            binary_num += pow(2, (2 - square_y) * 3 + (2 - square_x))

            if algorithm[binary_num] == "#":
                new_lights.add((x + 1, y + 1))

    return new_lights


def main():
    algorithm, image = get_algorithm_with_image()

    lights = {(x, y) for y, row in enumerate(image) for x, pixel in enumerate(row) if pixel == '#'}
    for step in count(start=1, step=1):
        lights = enhance(step, lights, algorithm)
        if step == 50:
            break

    print(len(lights))


if __name__ == '__main__':
    main()
