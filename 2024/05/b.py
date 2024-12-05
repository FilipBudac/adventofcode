def is_ordered(rules, update):
    return all((a, b) in rules for a, b in zip(update, update[1:]))


raw_rules, raw_updates = open("input.txt").read().split("\n\n")

rules = [tuple(r.split('|')) for r in raw_rules.strip().split('\n')]
updates = [u.split(',') for u in raw_updates.strip().split('\n')]


res = 0
for update in updates:
    if is_ordered(rules, update):
        continue
    for a in update:
        if sum((a, b) in rules for b in update) == len(update) // 2:
            res += int(a)

print(res)
