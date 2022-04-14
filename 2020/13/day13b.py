from sympy.ntheory.modular import crt

with open('input.txt') as file:
    busses = [(int(bus), t) for t, bus in enumerate(file.readlines()[1].split(',')) if bus != 'x']

a, m = [], []
for bus, t in busses:
    m.append(bus)
    a.append(-t)

print(crt(m, a)[0])
