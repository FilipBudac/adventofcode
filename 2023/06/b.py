import re


with open('input.txt') as file:
    time = int(''.join(re.findall(r'\d+', file.readline())))
    distance = int(''.join(re.findall(r'\d+', file.readline())))

print(len([(time - hold) * hold for hold in range(time) if (time - hold) * hold > distance]))
