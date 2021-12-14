from collections import defaultdict

STEPS = 10


def get_template_with_insertions():
    with open('input.txt') as f:
        template = None
        while line := f.readline().strip():
            template = line
        insertions = [insertion.strip().split(' -> ') for insertion in f.readlines()]
    return template, insertions


def get_insertion_guide(insertions):
    insertion_map = {}
    for insertion in insertions:
        subs, char = insertion
        subs_a, subs_b = subs
        insertion_map[(subs_a, subs_b)] = ((subs_a, char), (char, subs_b))

    return insertion_map


def update_replacements(new_replacements, insertion_pair, count):
    pair_a, pair_b = insertion_pair
    new_replacements[pair_a] += count
    new_replacements[pair_b] += count


def replace(insertion_guide, replacements):
    new_replacements = defaultdict(int)
    for replacement in replacements:
        update_replacements(new_replacements, insertion_guide[replacement], replacements[replacement])

    return new_replacements


def get_replacements(template):
    initial_replacements = defaultdict(int)
    for char, other in zip(template, template[1:]):
        initial_replacements[(char, other)] += 1

    return initial_replacements


def calc_result(replacements):
    char_counts = defaultdict(int)
    for pair, count in replacements.items():
        char, _ = pair
        char_counts[char] += count
    max_c = max(char_counts.values()) - 1
    min_c = min(char_counts.values())

    return max_c - min_c


def main():
    template, insertions = get_template_with_insertions()

    insertion_guide = get_insertion_guide(insertions)
    replacements = get_replacements(template)
    
    for _ in range(STEPS):
        replacements = replace(insertion_guide, replacements)

    print(calc_result(replacements))


if __name__ == '__main__':
    main()
