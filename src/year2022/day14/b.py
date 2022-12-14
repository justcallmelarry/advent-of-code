import collections
from dataclasses import dataclass, field

import utils
from injection import input_injection


@dataclass
class Rocks:
    # no start_h is needed as sand always starts at 0
    start_w: int = 10**6
    end_w: int = 0
    end_h: int = 0
    coords: set[tuple[int, int]] = field(default_factory=set)


def get_rocks(_input: str) -> Rocks:
    rocks = Rocks()
    for line in _input.splitlines():
        coords = line.split(" -> ")
        for i in range(1, len(coords)):
            coord_span = sorted([utils.ints(coords[i - 1]), utils.ints(coords[i])])
            rocks.coords.update(set(tuple(x) for x in coord_span))  # type: ignore
            x_update = coord_span[0][0] != coord_span[1][0]
            y_update = coord_span[0][1] != coord_span[1][1]

            if y_update:
                for value in range(coord_span[0][1], coord_span[1][1]):
                    c = (coord_span[0][0], value)
                    rocks.coords.add(c)
            if x_update:
                for value in range(coord_span[0][0], coord_span[1][0]):
                    rocks.coords.add((value, coord_span[0][1]))

            rocks.end_w = max(rocks.end_w, coord_span[0][0], coord_span[1][0])
            rocks.start_w = min(rocks.start_w, coord_span[0][0], coord_span[1][0])
            rocks.end_h = max(rocks.end_h, coord_span[0][1], coord_span[1][1])

    return rocks


def update_grid(grid: list[list], coords: tuple[int, int], fill: str) -> None:
    grid[coords[1]][coords[0]] = fill


@input_injection
def main(_input: str) -> str:

    rocks = get_rocks(_input)

    grid = utils.make_grid(rocks.end_h + 3, (rocks.end_w - rocks.start_w + 1) * 9, fill=".")

    half_grid_w = len(grid[0]) // 2
    rocks.coords = set([(rock[0] - rocks.start_w + half_grid_w, rock[1]) for rock in rocks.coords])
    sand_start = (500 - rocks.start_w + half_grid_w, 0)

    for i in range(len(grid[0])):
        grid[-1][i] = "#"

    for rock in rocks.coords:
        update_grid(grid, rock, "#")

    update_grid(grid, sand_start, "+")
    sand_x, sand_y = sand_start
    sand_grains = 0
    previous_sand_grains = -1

    def inbounds(x: int, y: int) -> bool:
        return all(
            [
                x >= 0,
                y <= len(grid) -1,
                y >= 0,
                x <= len(grid[0]) - 1,
            ]
        )

    def get_value(x: int, y: int) -> str:
        if not inbounds(x, y):
            return "inf"
        return grid[y][x]

    while True:
        sand_cur_pos = (sand_x, sand_y)
        under_straight = sand_x, sand_y + 1
        under_left = sand_x - 1, sand_y + 1
        under_right = sand_x + 1, sand_y + 1

        if get_value(*under_straight) == ".":
            sand_y += 1
            continue

        if get_value(*under_left) == ".":
            sand_y += 1
            sand_x -= 1
            continue

        elif get_value(*under_right) == ".":
            sand_y += 1
            sand_x += 1
            continue

        if sand_grains == previous_sand_grains:
            break

        if get_value(sand_x, sand_y) == "+":
            update_grid(grid, sand_cur_pos, "o")
            sand_grains += 1
            break

        previous_sand_grains = sand_grains

        foundation = (
            get_value(*under_left),
            get_value(*under_straight),
            get_value(*under_right),
        )
        if all(x not in foundation for x in (".", "inf")):
            update_grid(grid, sand_cur_pos, "o")
            sand_grains += 1

        sand_x, sand_y = sand_start

    if False:  # DEBUG OUTPUT
        for r in grid:
            print("".join(r))

    return str(sand_grains)


if __name__ == "__main__":
    print(main())
