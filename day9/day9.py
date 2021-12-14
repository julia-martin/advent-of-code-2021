# parse_input returns 2D array of ints
def parse_input(path):
    heightmap = []
    with open(path) as f:
        for line in f:
            heightmap.append([int(h) for h in line.strip()])
    return heightmap

# Returns answer to Pt 1 and low point locations for use in Pt 2
def calc_pt1(heightmap):
    risk_levels = []
    low_locs = []
    num_rows = len(heightmap)
    num_cols = len(heightmap[0])
    for row in range(num_rows):
        for col in range(num_cols):
            is_low = True
            curr = heightmap[row][col]
            if (row > 0) and (heightmap[row-1][col] <= curr):
                is_low = False
            elif (col > 0) and (heightmap[row][col-1] <= curr):
                is_low = False
            elif (row < num_rows - 1) and (heightmap[row+1][col] <= curr):
                is_low = False
            elif (col < num_cols - 1) and (heightmap[row][col+1] <= curr):
                is_low = False

            if is_low:
                risk_levels.append(curr + 1)
                low_locs.append([row, col])

    return sum(risk_levels), low_locs

def calc_pt2(low_locs, heightmap):
    basins = {}
    for loc in low_locs:
        basins[','.join(map(str, loc))] = []

    num_rows = len(heightmap)
    num_cols = len(heightmap[0])
    for row in range(num_rows):
        for col in range(num_cols):
            curr = heightmap[row][col]

            if curr == 9:
                continue
            for basin in basins.values():
                if coords_to_str([row, col]) in basin:
                    continue

            lowest = curr
            curr_row = row
            curr_col = col
            curr_coord = coords_to_str([curr_row, curr_col])
            visited_coords = [curr_coord]

            while curr_coord not in basins.keys():
                if (curr_row > 0) and (heightmap[curr_row-1][curr_col] < lowest):
                    lowest = heightmap[curr_row-1][curr_col]
                    curr_row -= 1
                if (curr_col > 0) and (heightmap[curr_row][curr_col-1] < lowest):
                    lowest = heightmap[curr_row][curr_col-1]
                    curr_col -= 1
                if (curr_row < num_rows - 1) and (heightmap[curr_row+1][curr_col] < lowest):
                    lowest = heightmap[curr_row+1][curr_col]
                    curr_row += 1
                if (curr_col < num_cols - 1) and (heightmap[curr_row][curr_col+1] < lowest):
                    lowest = heightmap[curr_row][curr_col+1]
                    curr_col += 1

                curr_coord = coords_to_str([curr_row, curr_col])
                visited_coords.append(curr_coord)

            basins[curr_coord].extend([c for c in visited_coords if c not in basins[curr_coord]])

    sizes = sorted([len(v) for k,v in basins.items()], reverse=True)
    return sizes[0] * sizes[1] * sizes[2]

def coords_to_str(coords):
    return ','.join(map(str, coords))

hm = parse_input('input.txt')
pt1_answer, low_locs = calc_pt1(hm)
result = calc_pt2(low_locs, hm)
print(result)