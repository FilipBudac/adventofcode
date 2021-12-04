class Winner(Exception):
    pass


class Board:
    valid_positions = [
        [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
        [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)],
        [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
        [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)],
        [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)],
    ]

    def __init__(self, rows):
        self.rows = rows
        self.positions = []
        self.last_number = None

    def verify_board(self):
        for row_positions in self.valid_positions:
            row_check = all(position in self.positions for position in row_positions)
            if row_check:
                return True

        transposed_valid_positions = list(map(list, zip(*self.valid_positions)))
        for row_positions in transposed_valid_positions:
            row_check = all(position in self.positions for position in row_positions)
            if row_check:
                return True

        return False

    def update_board(self, num):
        for i, row in enumerate(self.rows):
            try:
                j = row.index(num)
            except ValueError:
                continue

            self.positions.append((i, j))
            break

    def calc_result(self):
        total = 0
        for row_positions in self.valid_positions:
            for position in row_positions:
                if position not in self.positions:
                    i, j = position
                    val = self.rows[i][j]
                    total += int(val)

        return total * self.last_number

    def set_last_number(self, num):
        self.last_number = int(num)


def get_boards(f):
    boards = []

    data = f.readlines()
    for i in range(0, len(data), 6):
        board_data = data[i:i + 6]
        board_data = board_data[1:]
        board = []
        for row in board_data:
            numbers = row.strip().split()
            board.append(numbers)
        board = Board(board)
        boards.append(board)

    return boards


def main():
    with open('input.txt') as f:
        numbers = f.readline().strip().split(',')
        boards = get_boards(f)

    winner_boards = []
    for number in numbers:
        for board in boards:
            if board in winner_boards:
                continue
            board.update_board(number)
            winner = board.verify_board()
            if winner:
                board.set_last_number(number)
                winner_boards.append(board)

    last_winner = winner_boards[-1]
    print(last_winner.calc_result())


if __name__ == '__main__':
    main()
