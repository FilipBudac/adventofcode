with open('input.txt') as file:
    lines = [l.strip().split(': ') for l in file]

monkeys = {}
for (n, expr) in lines:
    if expr.isdigit():
        monkeys[n] = int(expr)
        continue
    l, o, r = expr.split()
    if l in monkeys and r in monkeys:
        monkeys[n] = eval(f"{monkeys[l]} {o} {monkeys[r]}")
        continue
    lines.append((n, expr))

print(monkeys['root'])
