with open('input.txt') as file:
    time = int(file.readline())
    busses = [int(bus) for bus in file.readline().split(',') if bus != 'x']

wait, bus = min((-time % bus, bus) for bus in busses)
print(wait * bus)
