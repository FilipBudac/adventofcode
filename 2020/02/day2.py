import re

with open('input.txt') as file:
    lines = [re.match(r'(\d+)-(\d+)\s(\w+):\s(\w+)', line).groups() for line in file]

print(sum(int(low) <= password.count(char) <= int(high) for (low, high, char, password) in lines))
