def parse_input(path):
    x_coords = []
    y_coords = []
    folds = []
    is_coord = True

    with open(path) as f:
        for line in f:
            if line == '\n':
                is_coord = False
                continue
            if is_coord:
                x, y = map(int, line.strip().split(','))
                x_coords.append(x)
                y_coords.append(y)
            else:
                folds.append(line.strip().replace('fold along ', ''))

        max_x = max(x_coords)
        max_y = max(y_coords)
        paper = [[False for _ in range(max_x+1)] for _ in range(max_y+1)]
        for idx, x in enumerate(x_coords):
            paper[y_coords[idx]][x] = True

    return paper, folds

def calc_pt1(paper, folds):
    first_fold = folds[0]
    new_paper = fold_once(first_fold, paper)
    return sum([sum(line) for line in new_paper])

def calc_pt2(paper, folds):
    new_paper = paper
    for fold in folds:
        new_paper = fold_once(fold, new_paper)
    return [['#' if val else '.' for val in row] for row in new_paper]

def fold_once(fold, paper):
    axis, num = fold.split('=')
    num = int(num)
    if axis == 'y':
        first_half = paper[:num]
        second_half = paper[num+1:]
    elif axis == 'x':
        first_half = [row[:num] for row in paper]
        second_half = [row[num+1:] for row in paper]

    folded_half = get_folded(second_half, axis, num)
    new_paper = []

    for row_i in range(len(first_half)):
        row = []
        for col_i in range(len(first_half[0])):
            row.append(first_half[row_i][col_i] or folded_half[row_i][col_i])
        new_paper.append(row)
    return new_paper

def get_folded(half, axis, num):
    folded_half = []
    if axis == 'y':
        for row_i in range(len(half)-1, -1, -1):
            folded_half.append(half[row_i])
    elif axis == 'x':
        folded_half = [list(reversed(line)) for line in half]
    return folded_half

paper, folds = parse_input('input.txt')
result = calc_pt2(paper, folds)
for line in result:
    print(line)