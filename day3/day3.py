from collections import defaultdict

def parse_input(path):
    with open(path) as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
    return lines

def calc_pt1(lines):
    ones = defaultdict(int)
    for line in lines:
        for i, digit in enumerate(line):
            if digit == '1':
                ones[i] += 1
    gamma = ''
    epsilon = ''
    for i in range(len(lines[0])):
        if ones[i] > len(lines) / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    power = int(gamma, 2) * int(epsilon, 2)
    return power

def calc_pt2(numbers):
    og_rating = get_rating(numbers, 'oxygen')
    c02_rating = get_rating(numbers, 'c02')
    return og_rating * c02_rating

def get_rating(numbers, rating):
    idx = 0
    while (idx < len(numbers[0])) and (len(numbers) > 1):
        num_ones, num_zeros = get_counts(numbers, idx)
        if num_ones >= num_zeros:
            if rating == 'oxygen':
                numbers = [n for n in numbers if n[idx] == '1']
            elif rating == 'c02':
                numbers = [n for n in numbers if n[idx] == '0']
        else:
            if rating == 'oxygen':
                numbers = [n for n in numbers if n[idx] == '0']
            elif rating == 'c02':
                numbers = [n for n in numbers if n[idx] == '1']
        idx += 1

    return int(numbers[0], 2)

def get_counts(numbers, idx):
    num_ones = list(map(lambda x: x[idx], numbers)).count('1')
    num_zeros = len(numbers) - num_ones
    return num_ones, num_zeros


input = parse_input('input.txt')
result1 = calc_pt1(input)
result2 = calc_pt2(input)
print(result1)
print(result2)