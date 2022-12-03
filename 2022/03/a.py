with open('input.txt') as file:
    rucks = [*map(str.rstrip, file)]

tot = 0
for r in rucks:
    item = (set(r[:len(r) // 2]) & set(r[len(r) // 2:])).pop()
    if item.islower():
        tot += ord(item) - ord('a') + 1
    else:
        tot += ord(item) - ord('A') + 26 + 1
print(tot)

