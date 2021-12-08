def get_signal_patterns():
    with open('input.txt') as f:
        patterns = [line.split(' | ') for line in f.readlines()]
        patterns = [[inputs.split(' '), outputs.split(' ')] for inputs, outputs in patterns]

    return patterns


def a():
    c = 0
    for inputs, outputs in get_signal_patterns():
        for output in outputs:
            if len(output.strip()) in (2, 3, 4, 7):
                c += 1
    print(c)


def main():
    a()


if __name__ == '__main__':
    main()
