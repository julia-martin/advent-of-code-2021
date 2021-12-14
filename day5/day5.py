def calculate(file_path):
    xs = []
    ys = []
    with open(file_path) as f:
        # Find dimensions
        for line in f:
            line = line.strip().split(' -> ')
            for point in line:
                x, y = point.split(',')
                xs.append(int(x))
                ys.append(int(y))
    max_x, max_y = max(xs), max(ys)

    # Create square floor
    floor = [[0 for i in range(max_x + 1)] for j in range(max_y + 1)]
    # Loop through lines
    idx = 0
    while idx < len(xs):
        # Get line points
        start_x, start_y = xs[idx], ys[idx]
        end_x, end_y = xs[idx+1], ys[idx+1]
        # Mark crossed lines
        if (start_x == end_x):
            for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
                floor[y][start_x] += 1
        elif (start_y == end_y):
            for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                floor[start_y][x] += 1
        # Pt 2: Diagonal lines
        elif abs(start_x - end_x) == abs(start_y - end_y):
            x_inc = 1 if start_x < end_x else -1
            y_inc = 1 if start_y < end_y else -1
            curr_x = start_x
            curr_y = start_y
            while True:
                floor[curr_y][curr_x] += 1
                if (curr_x == end_x) or (curr_y == end_y):
                    break
                curr_x += x_inc
                curr_y += y_inc

        idx += 2

    return len([x for row in floor for x in row if x >= 2])


result = calculate('input.txt')
print(result)
