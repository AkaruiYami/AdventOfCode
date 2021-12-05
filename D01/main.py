def solution1(m):
    """Count the number of increases from given list m."""
    return [int(m[i]) > int(m[i - 1]) for i in range(1, len(m))].count(True)

def solution2(m):
    """Count the number of increases from each sum of 3 number from give list"""
    new_list = [int(m[i-2]) + int(m[i-1]) + int(m[i]) for i in range(2, len(m))]
    return solution1(new_list)

if __name__ == "__main__":
    with open("D01/input.txt") as f:
        _input = f.read().splitlines()

    print(solution2(_input))
