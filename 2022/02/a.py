with open('input.txt') as file:
    rounds = [line.split() for line in file]

# 3 : 1
# 1 : 2
# 2 : 3

tot = 0
for (opp, you) in rounds:
    opp = int(opp.translate(str.maketrans("ABC", "123")))
    you = int(you.translate(str.maketrans("XYZ", "123")))
    if opp % 3 + 1 == you:
        tot += 6
    elif opp == you:
        tot += 3
    tot += you

print(tot)
