import os


def is_low_point(x, adjacents):
    return all(x < value for value in adjacents.values())


def get_adjacents(heightmap, ix, iy):
    return {
        "left": heightmap[iy][ix - 1] if ix - 1 >= 0 else 10,
        "right": heightmap[iy][ix + 1] if ix + 1 < len(heightmap[iy]) else 10,
        "up": heightmap[iy - 1][ix] if iy - 1 >= 0 else 10,
        "down": heightmap[iy + 1][ix] if iy + 1 < len(heightmap) else 10,
    }


def expand_basin(heightmap, point):
    basin_points = set()
    edge_points = [point]

    while edge_points:
        ix, iy = edge_points.pop()

        if (ix, iy) in basin_points:
            continue

        curr_height = heightmap[iy][ix]
        adjacents = get_adjacents(heightmap, ix, iy)
        if curr_height < adjacents["left"] < 9:
            edge_points.append((ix - 1, iy))
        if curr_height < adjacents["right"] < 9:
            edge_points.append((ix + 1, iy))
        if curr_height < adjacents["up"] < 9:
            edge_points.append((ix, iy - 1))
        if curr_height < adjacents["down"] < 9:
            edge_points.append((ix, iy + 1))

        basin_points.add((ix, iy))

    return len(basin_points)


def solution1(heightmap):
    total_risk = 0
    for iy, y in enumerate(heightmap):
        for ix, x in enumerate(y):
            adjacents = get_adjacents(heightmap, ix, iy)
            total_risk += (1 + x) if is_low_point(x, adjacents) else 0
    return total_risk


def solution2(heightmap):
    low_points = list()
    for iy, y in enumerate(heightmap):
        for ix, x in enumerate(y):
            adjacents = get_adjacents(heightmap, ix, iy)
            if is_low_point(x, adjacents):
                low_points.append((ix, iy))

    basins_size = [expand_basin(heightmap, point) for point in low_points]
    basins_size.sort(reverse=True)
    return basins_size[0] * basins_size[1] * basins_size[2]


if __name__ == "__main__":
    # Find dir address where the current code located and read input.txt from the dir
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "input.txt")) as file:
        data = file.read().splitlines()
    heightmap = [[int(x) for x in y] for y in data]

    print(solution1(heightmap))
    print(solution2(heightmap))
