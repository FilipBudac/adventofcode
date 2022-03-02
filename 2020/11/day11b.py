from copy import deepcopy

FLOOR, EMPTY, OCCUPIED = '.L#'
DELTAS = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]


def calc_pos(pos, delta):
    return tuple(a + b for a, b in zip(pos, delta))


def get_adjacent_occupied_seats(p_x, p_y, seats):
    total = 0
    for d_x, d_y in DELTAS:
        x, y = p_x + d_x, p_y + d_y

        while (x, y) in seats:
            if seats.get((x, y)) != FLOOR:
                if seats.get((x, y)) == OCCUPIED:
                    total += 1
                break

            x += d_x
            y += d_y

    return total


with open('input.txt') as file:
    seats = {(i, j): symbol for i, line in enumerate(file) for j, symbol in enumerate(list(line.strip()))}

while True:
    new_seats = deepcopy(seats)
    for pos, seat in seats.items():
        occ = get_adjacent_occupied_seats(*pos, seats)
        if seat == EMPTY and occ == 0:
            new_seats[pos] = OCCUPIED
        if seat == OCCUPIED and occ >= 5:
            new_seats[pos] = EMPTY
    if seats == new_seats:
        break
    seats = new_seats

print(sum(seat == OCCUPIED for seat in seats.values()))
