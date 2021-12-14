from statistics import median

def parse_input(path):
    with open(path) as f:
        positions = list(map(int, f.read().split(',')))
    return positions

def calc_pt1(input):
    med = median(input)
    return sum([abs(med - pos) for pos in input])

def calc_pt2(input):
    fuels = []
    for dest in range(min(input) + 1, max(input)):
        fuel = 0
        for pos in input:
            diff = abs(dest - pos)
            fuel += (diff / 2) * (1 + diff)
        fuels.append(fuel)
    return min(fuels)

input = parse_input('input.txt')
result = calc_pt1(input)
print(result)