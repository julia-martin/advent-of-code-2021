def has_winner(board):
    # Horizontal
    for line in board:
        if all(item['drawn'] for item in line):
            return True
    # Vertical
    for i in range(len(board[0])):
        if all(line[i]['drawn'] for line in board):
            return True

    return False


def parse_inputs(input_path, boards_path):
    with open(input_path) as f:
        nums_to_draw = list(map(int, f.read().split(',')))

    boards = []
    curr_board = []
    with open(boards_path) as f:
        for line in f:
            nums = list(map(int, line.split()))
            if len(nums) == 0:
                boards.append(curr_board)
                curr_board = []
            else:
                new_line = [{'val': val, 'drawn': False} for val in nums]
                curr_board.append(new_line)
        boards.append(curr_board)

    return nums_to_draw, boards


def draw_nums(nums_to_draw, boards):
    winning_boards = [False for board in boards]

    for num in nums_to_draw:
        for b_idx, board in enumerate(boards):
            for line in board:
                for item in line:
                    if item['val'] == num:
                        item['drawn'] = True
            if has_winner(board):
                winning_boards[b_idx] = True
                if all(winning_boards):
                    sum_unmarked = sum([item['val'] for line in board for item in line if not item['drawn']])
                    return sum_unmarked * num


nums_to_draw, boards = parse_inputs('input.txt', 'boards.txt')
score = draw_nums(nums_to_draw, boards)
print(score)
