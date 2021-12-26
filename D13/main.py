import os
import re


def get_instructions(data):
    """Return a dictionary of instructions containing dots and folds"""
    dots = list()
    folds = list()
    data = list(filter(None, data))
    fold_instruction_pattern = re.compile(r"fold along ([xy])=(\d+)")
    for line in data:
        pattern_match = fold_instruction_pattern.match(line)
        if pattern_match is None:
            dots.append(tuple(map(int, line.split(","))))
            continue

        if pattern_match.group(1) == "x":
            folds.append((int(pattern_match.group(2)), None))
        else:
            folds.append((None, int(pattern_match.group(2))))
    return {"dots": dots, "folds": folds}


def fold_at(dots, x=None, y=None):
    """Reflect the dots according to given axis. Dots that are directly on the fold line will be discard."""

    new_dots = set()
    for dot_x, dot_y in dots:
        if dot_x == x != None or dot_y == y != None:
            continue
        new_x = dot_x + 2 * min(0, x - dot_x) if x else dot_x
        new_y = dot_y + 2 * min(0, y - dot_y) if y else dot_y
        new_dots.add((new_x, new_y))
    return list(new_dots)


def draw_map(dots, fill_char="#", empty_char="."):
    "Draw a dot map where the dots will be represented by fill_char and the empty space between the dot will be represented by empty_char."
    width = max(dot[0] for dot in dots)
    height = max(dot[1] for dot in dots)
    for y in range(height + 1):
        row = ""
        for x in range(width + 1):
            row += fill_char if (x, y) in dots else empty_char
        print(row)


def solution1(instructions):
    dots = instructions["dots"]
    folds = instructions["folds"]
    new_dots = fold_at(dots, *folds[0])
    return len(new_dots)


def solution2(instructions):
    dots = instructions["dots"]
    folds = instructions["folds"]
    while folds:
        dots = fold_at(dots, *folds.pop(0))
    draw_map(dots, fill_char="█")


if __name__ == "__main__":
    # Find dir address where the current code located and read input.txt from the dir
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()
    instructions = get_instructions(data)

    print(solution1(instructions))
    solution2(instructions)
