def solution1(l):
    """Count the number of increases from given list m."""
    return [int(l[i]) > int(l[i - 1]) for i in range(1, len(l))].count(True)


def solution2(l):
    """Count the number of increases from each sum of 3 number from give list"""
    new_list = [int(l[i - 2]) + int(l[i - 1]) + int(l[i]) for i in range(2, len(l))]
    return solution1(new_list)


if __name__ == "__main__":
    with open("D01/input.txt") as f:
        _input = f.read().splitlines()

    print(solution1(_input))
    print(solution2(_input))
