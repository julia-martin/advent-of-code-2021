def calc_pt1(path):
    counter = 0
    prev = None
    with open(path) as f:
        for line in f:
            if prev and int(line) > prev:
                counter += 1
            prev = int(line)

    return counter

def calc_pt2(path):
    counter = 0
    with open(path) as f:
        lines = list(map(lambda x: int(x.strip()), f.readlines()))
        prev_total = None
        for idx, val in enumerate(lines[:-2]):
            total = sum(lines[idx:idx+3])
            if prev_total and total > prev_total:
                counter += 1
            prev_total = total

    return counter

result = calc_pt2('input.txt')
print(result)