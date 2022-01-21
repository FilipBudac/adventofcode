import re


def count_bags(bag):
    count = []
    for b in rules[bag]:
        count.append(rules[bag][b] * (1 + count_bags(b)))
    return sum(count)


rules = {}
with open('input.txt') as file:
    for line in file:
        bag, contents = line.strip().split(' bags contain ')
        rules[bag] = {bag: int(num) for num, bag in re.findall(r'(\d+) (\w+ \w+)', contents)}

print(count_bags('shiny gold'))
