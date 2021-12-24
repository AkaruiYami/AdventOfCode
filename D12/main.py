import os
from collections import defaultdict


def get_cave_map(data):
    """Return a dictionary of cave_entry:set(cave_connections)."""
    cave_map = defaultdict(set)
    for line in data:
        a, b = line.split("-")
        if a != "end" and b != "start":
            cave_map[a].add(b)
        if b != "end" and a != "start":
            cave_map[b].add(a)
    return cave_map


def travel(cave_map, curr_loc="start", travelled_path=None, repeatable=False):
    """Travel through all cave according to cave_map and return the number of path that reached to the end. It will only travel to lowercase cave only once unless repeatable is set to True."""
    if travelled_path is None:
        travelled_path = list()

    if curr_loc == "end":
        return 1

    # check if we visit small cave
    if curr_loc.islower() and curr_loc in travelled_path:
        if repeatable:
            repeatable = False
        else:
            return 0

    travelled_path.append(curr_loc)

    count = 0
    for loc in cave_map[curr_loc]:
        count += travel(cave_map, loc, travelled_path.copy(), repeatable)

    return count


def solution1(cave_map):
    return travel(cave_map)


def solution2(cave_map):
    return travel(cave_map, repeatable=True)


if __name__ == "__main__":
    # Find dir address where the current code located and read input.txt from the dir
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()
    cave_map = get_cave_map(data)

    print(solution1(cave_map))
    print(solution2(cave_map))
