from grid import Sparse
from injection import input_injection
from year2022.day14.a import fill_sand, get_rocks


@input_injection
def main(_input: str) -> str:
    rocks = get_rocks(_input)

    grid = Sparse(default=".")

    for i in range(rocks.end_w * 2):  # set arbitrary amount of flooring
        grid.update((i, rocks.end_h + 2), "#")
        grid.update((-i, rocks.end_h + 2), "#")

    for rock in rocks.coords:
        grid.update(rock, "#")

    sand = fill_sand(grid)

    return str(sand)


if __name__ == "__main__":
    print(main())
