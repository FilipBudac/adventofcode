import sympy


with open('input.txt') as file:
    lines = [l.strip().split(': ') for l in file]

CALC = {
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a / b,
}

monkeys = {'humn': sympy.Symbol('unknown')}
for (n, expr) in lines:
    if n in monkeys:
        continue
    if expr.isdigit():
        monkeys[n] = int(expr)
        continue
    l, o, r = expr.split()
    if l in monkeys and r in monkeys:
        monkeys[n] = CALC[o](monkeys[l], monkeys[r])
        if n == 'root':
            monkeys[n] = sympy.solve(monkeys[l] - monkeys[r]).pop()
            break
    lines.append((n, expr))

print(monkeys['root'])
