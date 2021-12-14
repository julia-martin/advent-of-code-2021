def parse_input(path):
    with open(path) as f:
        timers = list(map(int, f.read().split(',')))
    return timers

def init_counts(timers):
    counts = {}
    for x in range(9):
        counts[x] = 0

    for val in timers:
        counts[val] += 1

    return counts

def simulate(timers, num_days):
    counts = init_counts(timers)
    for day in range(num_days):
        num_zeros = counts[0]
        counts[0] = 0
        for val in counts:
            if val > 0:
                counts[val-1] += counts[val]
                counts[val] = 0
        counts[8] += num_zeros
        counts[6] += num_zeros

    return sum(counts.values())


timers = parse_input('input.txt')
print(simulate(timers, 256))