HORIZONTAL_MOVEMENT = {"up": -1, "down": 1}


def get_instruction(l):
    """Get a set of instructions (Movement, Value) from given list of strings."""
    instructions = []
    for item in l:
        data = item.split()
        instructions.append((data[0], int(data[1])))
    return instructions


def solution1(l):
    """Return X * Y after following a set of instructions."""
    position = [0, 0]
    for move, value in get_instruction(l):
        if move == "forward":
            position[0] += value
        else:
            position[1] += HORIZONTAL_MOVEMENT[move] * value
    return position[0] * position[1]


def solution2(l):
    """Return X * Depth after following a set of instructions."""
    aim = 0
    depth = 0
    x = 0
    for move, value in get_instruction(l):
        if move == "forward":
            x += value
            depth += aim * value
        else:
            aim += HORIZONTAL_MOVEMENT[move] * value
    return x * depth


if __name__ == "__main__":
    with open("D02/input.txt") as f:
        _input = f.read().splitlines()

    print(solution1(_input))
    print(solution2(_input))
