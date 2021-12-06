from collections import Counter


def get_initial_state():
    with open('input.txt') as f:
        initial_state = list(map(int, f.readline().split(',')))

    return initial_state


def calc_result(state):
    return sum(val for val in state.values())


def progress_n_days(n):
    d = Counter(get_initial_state())

    for day in range(0, n, 8):
        d = progress_next_8_days(d)

    return d


def progress_next_8_days(d):
    state = Counter()

    state[0] = d[8] + d[1]
    state[1] = d[2] + d[0]
    state[2] = d[3] + d[1]
    state[3] = d[4] + d[2]
    state[4] = d[5] + d[3]
    state[5] = d[6] + d[4]
    state[6] = d[7] + d[5] + d[0]
    state[7] = d[6]
    state[8] = d[0] + d[7]

    return state


def main():
    print(calc_result(progress_n_days(80)))
    print(calc_result(progress_n_days(256)))


if __name__ == '__main__':
    main()
