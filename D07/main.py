import os


def solution1(position_map):
    feul_spends = []
    for new_pos in range(max(position_map.keys()) // 2):
        feul_spends.append(
            sum(
                abs(new_pos - current_pos) * n
                for current_pos, n in position_map.items()
            )
        )
    return min(feul_spends)


def solution2(position_map):
    feul_spends = []
    for new_pos in range(max(position_map.keys()) // 2):
        feul_spends.append(
            sum(
                ((abs(new_pos - current_pos) * (1 + abs(new_pos - current_pos))) // 2)
                * n
                for current_pos, n in position_map.items()
            )
        )
    return min(feul_spends)


if __name__ == "__main__":
    # Find dir address where the current code located and read input.txt from the dir
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()
    horizontal_positions = list(map(int, data[0].split(",")))
    position_map = {
        pos: horizontal_positions.count(pos) for pos in set(horizontal_positions)
    }

    print(solution1(position_map))
    print(solution2(position_map))
