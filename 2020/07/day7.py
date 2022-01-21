import re


def count_colors(bag):
    bags = [rule for rule in rules if bag in rules[rule]]
    colors = {bag}
    for b in bags:
        colors |= {o for o in count_colors(b)}
    return colors


rules = {}
with open('input.txt') as file:
    for line in file:
        bag, contents = line.strip().split(' bags contain ')
        rules[bag] = {bag: int(num) for num, bag in re.findall(r'(\d+) (\w+ \w+)', contents)}

print(len(count_colors('shiny gold')) - 1)
