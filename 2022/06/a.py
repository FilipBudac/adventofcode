with open('input.txt') as file:
    buff = file.readline().rstrip()

for i in range(len(buff)):
    if len(set(buff[i: i + 4])) == 4:
        print(i + 4)
        break

