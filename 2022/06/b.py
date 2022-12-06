with open('input.txt') as file:
    buff = file.readline().rstrip()

for i in range(len(buff)):
    if len(set(buff[i: i + 14])) == 14:
        print(i + 14)
        break

