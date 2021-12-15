import sys


def get_risk_level_map():
    with open('input.txt') as f:
        risk_level_map = [list(map(int, list(line.strip()))) for line in f.readlines()]

    height = len(risk_level_map)
    width = len(risk_level_map[0])
    for _ in range(4):
        for row in risk_level_map:
            row.extend((x + 1) if x < 9 else 1 for x in row[-width:])

    for _ in range(4):
        for row in risk_level_map[-height:]:
            risk_level_map.append([(x + 1) if x < 9 else 1 for x in row])

    return risk_level_map


def main():
    risk_level_map = get_risk_level_map()
    height = len(risk_level_map)
    width = len(risk_level_map[0])

    costs_map = [[sys.maxsize for _ in range(width)] for _ in range(height)]

    row_sum = 0
    for i in range(width):
        costs_map[0][i] = row_sum + risk_level_map[0][i]
        row_sum = costs_map[0][i]

    col_sum = 0
    for i in range(height):
        costs_map[i][0] = col_sum + risk_level_map[i][0]
        col_sum = costs_map[i][0]

    for i in range(1, height):
        for j in range(1, width):
            costs_map[i][j] = risk_level_map[i][j] + min(costs_map[i - 1][j], costs_map[i][j - 1])

    print(costs_map[height - 2][width - 1] - costs_map[0][0])


if __name__ == '__main__':
    main()
