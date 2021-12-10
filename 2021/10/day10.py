SCORE_TABLE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

OPEN_BRACKETS = ['(', '{', '[', '<']
CLOSE_BRACKETS = [')', '}', ']', '>']


def get_lines():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    return lines


def main():
    lines = get_lines()

    total_score = 0
    for line in lines:
        stack = []
        for bracket in line:
            if bracket in OPEN_BRACKETS:
                stack.append(bracket)
            if bracket in CLOSE_BRACKETS:
                last_bracket = stack.pop()
                idx = CLOSE_BRACKETS.index(bracket)
                if last_bracket != OPEN_BRACKETS[idx]:
                    total_score += SCORE_TABLE[bracket]
                    break

    print(total_score)


if __name__ == '__main__':
    main()
