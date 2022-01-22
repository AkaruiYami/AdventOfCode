import os
from collections import defaultdict


def update_fish(fishes):
    new_fish_lib = defaultdict(int)
    for timer, n_fish in fishes.items():
        if timer == 0:
            timer = 7
            new_fish_lib[8] += n_fish
        new_fish_lib[timer - 1] += n_fish
    return new_fish_lib


def solution(fishes, days):
    fish_lib = fishes.copy()
    for _ in range(days):
        fish_lib = update_fish(fish_lib)

    return sum(fish_lib.values())


if __name__ == "__main__":
    # Find dir address where the current code located and read input.txt from the dir
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()
    lanternfishes = list(map(int, data[0].split(",")))
    fish_lib = {timer: lanternfishes.count(timer) for timer in set(lanternfishes)}

    print(solution(fish_lib, 80))
    print(solution(fish_lib, 256))
