import os


def increase_step(energy_grid):
    """Increase the energy level by 1. If the new energy level more than 9, it will change to 0. Will not change the given list and return new list instead."""
    new_energy_grid = list()
    for row in energy_grid:
        energy_row = [energy + 1 if energy < 9 else 0 for energy in row]
        new_energy_grid.append(energy_row)
    return new_energy_grid


def update_adjacents(energy_grid, flashed_points):
    """Update all energy levels that are adjacent to at least one of the flashed point. Will change the given 2D list and return a new list."""
    x_max = len(energy_grid[0])
    y_max = len(energy_grid)

    updated_points = set()
    adjacent_steps = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
        (1, 1),
    ]

    while flashed_points:
        x, y = flashed_points.pop()

        if (x, y) in updated_points:
            continue

        for dx, dy in adjacent_steps:
            x_adjacent = x + dx
            y_adjacent = y + dy
            if not (0 <= x_adjacent < x_max and 0 <= y_adjacent < y_max):
                continue

            energy_adjacent = energy_grid[y_adjacent][x_adjacent]
            energy_grid[y_adjacent][x_adjacent] = (
                energy_adjacent + 1 if 0 < energy_adjacent < 9 else 0
            )

            if energy_grid[y_adjacent][x_adjacent] != 0:
                continue

            flashed_points.append((x_adjacent, y_adjacent))

        updated_points.add((x, y))
    return energy_grid


def find_flashes(energy_grid):
    """Find 0 in the 2D list and return a list of the 0 position inside given 2D list."""
    flashed_points = list()
    for y, row in enumerate(energy_grid):
        for x, energy in enumerate(row):
            if energy != 0:
                continue
            flashed_points.append((x, y))
    return flashed_points


def solution1(energy_grid):
    total_flash = 0
    new_energy_grid = energy_grid.copy()
    for _ in range(100):
        new_energy_grid = increase_step(new_energy_grid)
        flashed_points = find_flashes(new_energy_grid)
        new_energy_grid = update_adjacents(new_energy_grid, flashed_points)
        total_flash += len(find_flashes(new_energy_grid))
    return total_flash


def solution2(energy_grid):
    steps = 0
    new_energy_grid = energy_grid.copy()
    is_all_flashed = lambda e: all([0 in set(e_r) and len(set(e_r)) == 1 for e_r in e])
    while not is_all_flashed(new_energy_grid):
        steps += 1
        new_energy_grid = increase_step(new_energy_grid)
        flashed_points = find_flashes(new_energy_grid)
        new_energy_grid = update_adjacents(new_energy_grid, flashed_points)
    return steps


if __name__ == "__main__":
    # Find dir address where the current code located and read input.txt from the dir
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()
    energy_grid = [[int(energy) for energy in row] for row in data]

    print(solution1(energy_grid))
    print(solution2(energy_grid))
