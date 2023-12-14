from collections import defaultdict


def is_small_cave(cave):
    return cave.islower()


def is_big_cave(cave):
    return cave.isupper()


def rec_find_paths(connections, current, visited, double_visit):
    if current == "end":
        return [["end"]]

    if is_small_cave(current):
        double_visit |= current in visited
        visited = visited | {current}
        
    paths = []
    for cave in connections[current]:
        if cave != "start" and (cave not in visited or not double_visit):
            paths.extend( [current] + p for p in rec_find_paths(connections, cave, visited, double_visit))


    return paths

def find_paths(connections):
    return rec_find_paths(connections, "start", set(), False)

def load_input():
    with open("input.txt", "r") as f:
        data = [tuple(line.strip().split("-")) for line in f.readlines()]
    connections = defaultdict(list)
    for from_, to in data:
        connections[from_].append(to)
        connections[to].append(from_)
    return connections