import re


with open('input.txt') as file:
    data = [list(map(int, re.match(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)', line).groups())) for line in file]


grid = {}
for id_, from_left, from_top, width, height in data:
    for x in range(height):
        for y in range(width):
            coord = (from_left + y + 1, from_top + x + 1)
            if coord in grid:
                grid[coord] = 'x'
            else:
                grid[coord] = id_

for id_, from_left, from_top, width, height in data:
    if all(grid[from_left + y + 1, from_top + x + 1] != 'x' for x in range(height) for y in range(width)):
        print(id_)

