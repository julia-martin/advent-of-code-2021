# import numpy as np

def parse_input(path):
    energies = []
    with open(path) as f:
      for line in f:
        energies.append([int(e) for e in line.strip()])

    return energies

def flash(arr, row, col, flashed):
    arr[row][col] += 1

    if arr[row][col] > 9:
        flashed.append([row, col])
        arr[row][col] = 0

        row_len = len(arr[0])
        if (row > 0) and (col > 0):
            flash(arr, row-1, col-1, flashed)
        if row > 0:
            flash(arr, row-1, col, flashed)
        if (row > 0) and (col < row_len - 1):
            flash(arr, row-1, col+1, flashed)
        if col > 0:
            flash(arr, row, col-1, flashed)
        if col < row_len - 1:
            flash(arr, row, col+1, flashed)
        if (row < len(arr) - 1) and (col > 0):
            flash(arr, row+1, col-1, flashed)
        if row < len(arr) - 1:
            flash(arr, row+1, col, flashed)
        if (row < len(arr) - 1) and (col < row_len - 1):
            flash(arr, row+1, col+1, flashed)
    return flashed

def calc_pt1(arr, num_steps):
    flash_count = 0
    for step in range(num_steps):
        flashed = []
        for row in range(len(arr)):
            for col in range(len(arr[0])):
                flashed = flash(arr, row, col, flashed)

        for row, col in flashed:
            arr[row][col] = 0
        flash_count += len(flashed)
    return flash_count

def calc_pt2(arr):
    step = 0
    while any([x != 0 for row in arr for x in row]):
        flashed = []
        for row in range(len(arr)):
            for col in range(len(arr[0])):
                flashed = flash(arr, row, col, flashed)

        for row, col in flashed:
            arr[row][col] = 0
        step += 1
    return step


input = parse_input('input.txt')
result = calc_pt2(input)
print(result)