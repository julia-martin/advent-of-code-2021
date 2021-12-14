def calc_pt1(path):
    h = 0
    v = 0

    with open(path) as f:
        for line in f:
            dimension, amt = line.split(' ')
            if dimension == 'forward':
                h += int(amt)
            elif dimension == 'down':
                v += int(amt)
            else:
                v -= int(amt)

    return h * v

def calc_pt2(path):
    h = 0
    v = 0
    aim = 0

    with open(path) as f:
        for line in f:
            dimension, amt = line.split(' ')
            if dimension == 'forward':
                h += int(amt)
                v += aim * int(amt)
            elif dimension == 'down':
                aim += int(amt)
            else:
                aim -= int(amt)

    return h * v

result = calc_pt2('input.txt')
print(result)