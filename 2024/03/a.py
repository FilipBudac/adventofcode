import re

with open("input.txt") as f:
    memory = f.read().rstrip()

print(sum(int(v1) * int(v2) for v1, v2 in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory)))
