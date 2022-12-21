from typing import Iterator

import utils
from injection import input_injection

adj = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]


def get_neighbours(coord: tuple[int, int, int]) -> Iterator[tuple[int, int, int]]:
    for neighbour in adj:
        yield (coord[0] + neighbour[0], coord[1] + neighbour[1], coord[2] + neighbour[2])


def get_surface(area: list[tuple[int, int, int]]) -> int:
    result = 0
    for coord in area:
        sides_covered = sum(1 for x in get_neighbours(coord) if x in area)
        result += 6 - sides_covered

    return result


@input_injection
def main(_input: str) -> str:
    lava_drop: list[tuple[int, int, int]] = [tuple(utils.ints(line)) for line in _input.splitlines()]  # type: ignore
    result = get_surface(lava_drop)

    return str(result)


if __name__ == "__main__":
    print(main())
