SCORE_TABLE = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

OPEN_BRACKETS = ['(', '{', '[', '<']
CLOSE_BRACKETS = [')', '}', ']', '>']


def get_lines():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    return lines


def main():
    scores = []
    for line in get_lines():
        stack = []
        for bracket in line:
            if bracket in OPEN_BRACKETS:
                stack.append(bracket)
            if bracket in CLOSE_BRACKETS:
                last_bracket = stack.pop()
                if last_bracket != OPEN_BRACKETS[CLOSE_BRACKETS.index(bracket)]:
                    break

        score = 0
        for bracket in reversed(stack):
            score = score * 5 + SCORE_TABLE[bracket]
        scores.append(score)

    scores = sorted(scores, reverse=True)
    print(scores[len(scores) // 4])


if __name__ == '__main__':
    main()
