from collections import defaultdict

def parse_input(path):
    rules = {}
    with open(path) as f:
        for idx, line in enumerate(f):
            if idx == 0:
                template = line.strip()
            elif idx >= 2:
                pair, insert = line.strip().split(' -> ')
                rules[pair] = insert
    return template, rules

def calc_pt2(template, rules):
    pair_counts = defaultdict(int)
    elem_counts = defaultdict(int)
    polymer = list(template)

    for i in range(len(polymer)-1):
        pair = ''.join(polymer[i:i+2])
        pair_counts[pair] += 1
        elem_counts[polymer[i]] += 1
    elem_counts[polymer[-1]] += 1

    for step in range(40):
        print(step)
        curr_pairs = {k: v for k, v in pair_counts.items() if v > 0}
        for pair, count in curr_pairs.items():
            if pair in rules:
                new_val = rules[pair]
                elem_counts[new_val] += count
                pair_counts[pair] -= count
                pair_counts[pair[0] + new_val] += count
                pair_counts[new_val + pair[1]] += count

    most, least = max(elem_counts.values()), min([v for v in elem_counts.values() if v > 0])
    return most - least


template, rules = parse_input('input.txt')
result = calc_pt2(template, rules)
print(result)