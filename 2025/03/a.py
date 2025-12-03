banks = list(map(str.strip, open('input.txt').readlines()))

output = 0
for b in banks:
    joltages = []
    for i in range(len(b) - 1):
        joltages.append(int(b[i] + str(max(list(map(int, b[i+1:]))))))
    output += max(joltages)

print(output)
