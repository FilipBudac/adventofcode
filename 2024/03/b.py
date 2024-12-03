import re

with open("input.txt") as f:
    memory = f.read().rstrip()

res = 0
enabled = True
for v1, v2, do, dont in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", memory):
    if do:
        enabled = True
    elif dont:
        enabled = False
    elif enabled:
        res += int(v1) * int(v2)

print(res)
