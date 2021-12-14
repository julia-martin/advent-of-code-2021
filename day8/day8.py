def parse_input(path):
    with open(path) as f:
        signals = []
        output_vals = []
        for line in f:
            first, second = line.split(' | ')
            signals.append(first.split())
            output_vals.append(second.split())
    return signals, output_vals

def calc_pt1(path):
    _, input = parse_input(path)
    count = 0
    for entry in input:
        for val in entry:
            if len(val) in [2, 3, 4, 7]:
                count += 1
    return count

def calc_pt2(path):
    pattern_to_digit = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4',
      'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}
    signals, outputs = parse_input(path)
    total = 0
    for idx, entry in enumerate(signals):
        mapping = get_mapping(entry)
        number_str = ''
        for pattern in outputs[idx]:
            decoded = ''
            for letter in pattern:
                decoded += mapping[letter]
            key = ''.join(sorted(decoded))
            digit = pattern_to_digit[key]
            number_str += digit
        total += int(number_str)
    return total

def get_mapping(entry):
    mapping = {}
    patterns = list(map(set, sorted(entry, key=len)))

    cf, acf, bcdf = patterns[0:3]
    mapping['a'] = cf ^ acf
    mapping['c'] = cf
    mapping['f'] = cf
    mapping['b'] = bcdf.difference(cf)
    mapping['d'] = bcdf.difference(cf)

    len_5 = [p for p in patterns if len(p) == 5]
    rem_5 = len_5.copy()
    for poss_b in mapping['b']:
        if len([p for p in len_5 if poss_b in p]) == 1:
            mapping['b'] = set(poss_b)
            mapping['d'].remove(poss_b)
            rem_5 = [p for p in rem_5 if poss_b not in p]

    ef = rem_5[0] ^ rem_5[1]
    mapping['f'] = cf & ef
    mapping['e'] = ef.difference(mapping['f'])
    mapping['b'] = mapping['b'].difference(mapping['e'])
    mapping['d'] = mapping['d'].difference(mapping['b'])
    f = list(mapping['f'])[0]
    for k, v in mapping.items():
        if k != 'f':
            v.discard(f)

    # Get g
    options = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    for val in mapping.values():
        options = options.difference(val)
    mapping['g'] = options
    # Reverse key and val, Change from set to string
    mapping = dict({(list(v)[0], k) for k, v in mapping.items()})

    return mapping

result = calc_pt2('input.txt')
print(result)