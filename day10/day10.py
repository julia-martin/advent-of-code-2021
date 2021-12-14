from statistics import median

def parse_input(path):
    with open(path) as f:
        lines = [line.strip() for line in f]
    return lines

complements = {')': '(', ']': '[', '}': '{', '>': '<'}

def calc_pt1(lines):
    score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in lines:
        stack = []
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            elif complements[char] == stack[-1]:
                stack.pop(-1)
            else:
                score += score_map[char]
                break
    return score

def calc_pt2(lines):
    incomplete_lines = []
    for line in lines:
        stack = []
        is_corrupt = False
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            elif complements[char] == stack[-1]:
                stack.pop(-1)
            else:
                is_corrupt = True
                break
        if not is_corrupt:
            incomplete_lines.append(line)

    open_to_close = {v:k for k, v in complements.items()}
    point_map = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for line in incomplete_lines:
        stack = []
        autocomplete = []
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            elif complements[char] == stack[-1]:
                stack.pop(-1)

        for remaining in reversed(stack):
            autocomplete.append(open_to_close[remaining])

        score = 0
        for char in autocomplete:
            score = score * 5 + point_map[char]
        scores.append(score)

    return median(scores)

input = parse_input('input.txt')
result = calc_pt2(input)
print(result)
