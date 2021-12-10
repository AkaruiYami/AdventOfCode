import os
from collections import defaultdict


def get_line(points):
    start = map(int, points[0].split(","))
    end = map(int, points[1].split(","))
    return tuple(start), tuple(end)


def add_line_to_world(line, world):
    start, end = line
    get_step = lambda l: 0 if l[0] == l[1] else (l[1] - l[0]) / abs(l[1] - l[0])
    x_step = get_step((start[0], end[0]))
    y_step = get_step((start[1], end[1]))
    distance = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
    for i in range(distance + 1):
        x = start[0] + i * x_step
        y = start[1] + i * y_step
        world[(x, y)] += 1


def count_overlap(world):
    counter = 0
    for point in world.values():
        if point > 1:
            counter += 1
    return counter


def solution1(lines):
    world = defaultdict(int)
    for start, end in lines:
        if start[0] == end[0] or start[1] == end[1]:
            add_line_to_world((start, end), world)
    return count_overlap(world)


def solution2(lines):
    world = defaultdict(int)
    for points in lines:
        add_line_to_world(points, world)
    return count_overlap(world)


if __name__ == "__main__":
    # Find dir address where the current code located and read input.txt from the dir
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()
    lines = [get_line(points.split("->")) for points in data]

    print(solution1(lines))
    print(solution2(lines))
