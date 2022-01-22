import os

pair_table = {"(": ")", "[": "]", "{": "}", "<": ">"}


def find_corrupted(lines):
    """Find and return a dictionary corrupted_line_index: corrupted_character"""
    corrupted_brackets = dict()
    for iline, line in enumerate(lines):
        open_brackets = list()
        for x in line:
            if x in pair_table.keys():
                open_brackets.append(x)
            elif x != pair_table[open_brackets.pop()]:
                corrupted_brackets[iline] = x
                break
        open_brackets.clear()
    return corrupted_brackets


def solution1(lines):
    point_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    corrupted_brackets = find_corrupted(lines)
    return sum(point_table[x] for x in corrupted_brackets.values())


def solution2(lines):
    point_table = {")": 1, "]": 2, "}": 3, ">": 4}
    corrupted_brackets = find_corrupted(lines)
    incomplete_lines = [
        x for ix, x in enumerate(lines) if ix not in corrupted_brackets.keys()
    ]

    # Search all missing brackets.
    missing_pair = list()
    for line in incomplete_lines:
        open_brackets = list()
        for x in line:
            if x in pair_table.keys():
                open_brackets.append(x)
            else:
                open_brackets.pop()
        missing_pair.append([pair_table[x] for x in open_brackets[::-1]])
        open_brackets.clear()

    # Calculate scores
    scores = list()
    for line in missing_pair:
        score = 0
        for x in line:
            score = score * 5 + point_table[x]
        scores.append(score)
    scores.sort()
    return scores[len(scores) // 2]


if __name__ == "__main__":
    # Find dir address where the current code located and read input.txt from the dir
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()
    lines = [[x for x in line] for line in data]

    print(solution1(lines))
    print(solution2(lines))
