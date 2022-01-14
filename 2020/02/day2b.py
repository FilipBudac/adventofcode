import re

with open('input.txt') as file:
    lines = [re.match(r'(\d+)-(\d+)\s(\w+):\s(\w+)', line).groups() for line in file]

print(sum((char == password[int(pos) - 1]) ^ (char == password[int(other_pos) - 1]) for (pos, other_pos, char, password) in lines))
