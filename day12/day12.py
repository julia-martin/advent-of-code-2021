# Does not return correct answer for this day's challenge

def parse_input(path):
    connections = {}
    with open(path) as f:
        for line in f:
            start, end = line.strip().split('-')
            if start in connections:
                connections[start].append(end)
            else:
                connections[start] = [end]

            if end in connections:
                connections[end].append(start)
            else:
                connections[end] = [start]
    return connections

def find_paths(connections, neighbors, paths=[], visited=[], curr_path=['start']):
    if len(neighbors) == 0:
        return paths

    neighbors_c = neighbors.copy()
    visited_c = visited.copy()
    curr_path_c = curr_path.copy()

    for neighbor in neighbors_c:
        if (neighbor == 'start') or (neighbor in visited_c):
            continue

        print(curr_path_c, neighbor)
        curr_path_c.append(neighbor)
        if neighbor == 'end':
            paths.append(curr_path_c)
            return

        if neighbor.islower():
            visited_c.append(neighbor)
        neighbors_c = connections[neighbor]
        # Call recursive
        find_paths(connections, neighbors_c, paths, visited_c, curr_path_c)

    return paths

connections = parse_input('small-example.txt')
print(connections)
result = find_paths(connections, connections['start'])
print(result)
