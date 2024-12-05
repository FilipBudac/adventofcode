def is_ordered(rules, update):
    return all((a, b) in rules for a, b in zip(update, update[1:]))


raw_rules, raw_updates = open("input.txt").read().split("\n\n")

rules = [tuple(r.split('|')) for r in raw_rules.strip().split('\n')]
updates = [u.split(',') for u in raw_updates.strip().split('\n')]


print(sum(int(u[len(u) // 2]) for u in updates if is_ordered(rules, u)))
