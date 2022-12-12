import collections
import string
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Iterator

import utils
from injection import input_injection
from models import Coords

height_index = "S" + string.ascii_lowercase + "E"
adjacenct_cells = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]


def get_index(char: str) -> int:
    return height_index.index(char)


def get_adjacent_cells(grid: list[list[int]], cell: tuple[int, int]) -> Iterator[tuple[tuple[int, int], int]]:
    max_x = len(grid[0])
    max_y = len((grid))
    for direction in adjacenct_cells:
        if 0 <= (cell[0] + direction[0]) < max_x and 0 <= cell[1] + direction[1] < max_y:
            if not 0 in direction:
                continue
            yield direction, grid[cell[1] + direction[1]][cell[0] + direction[0]]


def get_distance(grid: list[list[int]], initial: tuple[int, int]) -> int:
    seen: set = set()
    position: collections.deque[int] = collections.deque([*initial, 0])

    total_cells = len(grid) * len(grid[0])

    while position:
        x = position.popleft()
        y = position.popleft()
        steps = position.popleft()
        current_height = grid[y][x]
        seen.add((x, y))

        for direction, value in get_adjacent_cells(grid, (x, y)):
            current_pos = (x + direction[0], y + direction[1])
            if current_pos in seen:
                # skip already seen cells
                continue

            if abs(current_height - value) > 1:
                continue

            print(f"done with {len(seen)} / {total_cells}", end="\r")
            if value == get_index("E"):
                # whatever is the first to reach the end has the shortest value
                return steps + 1

            # add cell to end of queue
            position.append(current_pos[0])
            position.append(current_pos[1])
            position.append(steps + 1)

    return 0


@input_injection
def main(_input: str) -> str:
    start = Coords(name="start")
    grid: list[list[int]] = []

    for r, line in enumerate(_input.splitlines()):
        row: list[int] = []

        for c, char in enumerate(line):
            if char in "S":
                start.x = c
                start.y = r
            row.append(get_index(char))

        grid.append(row)

    distance = get_distance(grid, start.current_pos)

    return str(distance)


if __name__ == "__main__":
    main()
