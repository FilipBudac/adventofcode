with open('input.txt') as file:
    rounds = [line.split() for line in file]

# 1 : 3
# 2 : 1
# 3 : 2

tot = 0
for (opp, you) in rounds:
    opp = int(opp.translate(str.maketrans("ABC", "123")))
    you = int(you.translate(str.maketrans("XYZ", "123")))
    if you == 3:
        tot += 6 + opp % 3 + 1
    elif you == 2:
        tot += 3 + opp
    else:
        tot += (opp - 2) % 3 + 1
print(tot)
