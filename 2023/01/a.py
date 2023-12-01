with open('input.txt') as file:
    lines = map(str.rstrip, file.readlines())

print(sum(int(num[0] + num[-1]) for num in [[char for char in line if char.isnumeric()] for line in lines]))
