from copy import deepcopy

FLOOR, EMPTY, OCCUPIED = '.L#'
DELTAS = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]


def calc_pos(pos, delta):
    return tuple(a + b for a, b in zip(pos, delta))


with open('input.txt') as file:
    seats = {(i, j): symbol for i, line in enumerate(file) for j, symbol in enumerate(list(line.strip()))}

while True:
    new_seats = deepcopy(seats)
    for pos, seat in seats.items():
        occ = sum(seats.get(calc_pos(pos, delta)) == OCCUPIED for delta in DELTAS)
        if seat == EMPTY and occ == 0:
            new_seats[pos] = OCCUPIED
        if seat == OCCUPIED and occ >= 4:
            new_seats[pos] = EMPTY
    if seats == new_seats:
        break
    seats = new_seats

print(sum(seat == OCCUPIED for seat in seats.values()))
