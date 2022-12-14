from dataclasses import dataclass, field

import utils
from grid import Sparse
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


def fill_sand(grid: Sparse) -> int:
    sand_hole = (500, 0)
    grid.update(sand_hole, "+")

    total_sand = 0
    previous_sand_level = -1

    sand_x, sand_y = sand_hole

    while True:
        sand_cur_pos = (sand_x, sand_y)
        under_straight = sand_x, sand_y + 1
        under_left = sand_x - 1, sand_y + 1
        under_right = sand_x + 1, sand_y + 1

        if grid.get_value(under_straight) == ".":
            sand_y += 1
            continue

        if grid.get_value(under_left) == ".":
            sand_y += 1
            sand_x -= 1
            continue

        elif grid.get_value(under_right) == ".":
            sand_y += 1
            sand_x += 1
            continue

        if total_sand == previous_sand_level:
            return total_sand

        if grid.get_value(sand_cur_pos) == "+":
            grid.update(sand_cur_pos, "o")
            total_sand += 1
            return total_sand

        previous_sand_level = total_sand

        foundation = (
            grid.get_value(under_left),
            grid.get_value(under_straight),
            grid.get_value(under_right),
        )
        if all(x not in foundation for x in (".", grid.inf)):
            grid.update(sand_cur_pos, "o")
            total_sand += 1

        sand_x, sand_y = sand_hole


@input_injection
def main(_input: str) -> str:
    rocks = get_rocks(_input)

    grid = Sparse(height=rocks.end_h + 1, width=rocks.end_w + 1, default=".")

    for rock in rocks.coords:
        grid.update(rock, "#")

    total_sand = fill_sand(grid)

    return str(total_sand)


if __name__ == "__main__":
    print(main())
