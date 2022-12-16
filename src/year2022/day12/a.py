import collections
import string
from dataclasses import dataclass
from typing import Iterator

from injection import input_injection
from models import Coords

height_index = "S" + string.ascii_lowercase + "E"
adjacenct_cells = [(0, 1), (-1, 0), (1, 0), (0, -1)]


@dataclass
class Position:
    x: int
    y: int
    steps: int = 0

    @property
    def coords(self) -> tuple[int, int]:
        return self.x, self.y


def get_char_index(char: str) -> int:
    """
    Remember to read the puzzle, boys and girls
    """
    if char == "S":
        char = "a"
    if char == "E":
        char = "z"
    return height_index.index(char)


def get_adjacent_cells(grid: list[list[int]], cell: tuple[int, int]) -> Iterator[tuple[tuple[int, int], int]]:
    max_x = len(grid[0]) - 1
    max_y = len((grid)) - 1
    for direction in adjacenct_cells:
        new_x = cell[0] + direction[0]
        new_y = cell[1] + direction[1]
        if 0 <= new_x <= max_x and 0 <= new_y <= max_y:
            yield (new_x, new_y), grid[new_y][new_x]


def get_distance(grid: list[list[int]], initial: tuple[int, int], targets: list[tuple[int, int]]) -> Iterator[Position]:
    pos = Position(*initial)
    position: collections.deque[Position] = collections.deque([pos])
    seen: set = set([pos.coords])

    while position:
        pos = position.popleft()

        if pos.coords in targets:
            yield pos

        for coords, value in get_adjacent_cells(grid, pos.coords):
            current_height = grid[pos.y][pos.x]
            if coords in seen:
                continue

            too_high = value < current_height - 1
            if too_high:
                continue

            seen.add(coords)

            position.append(Position(*coords, steps=pos.steps + 1))


@input_injection
def main(_input: str) -> str:
    start = Coords(name="start")
    grid: list[list[int]] = []

    for r, line in enumerate(_input.splitlines()):
        row: list[int] = []

        for c, char in enumerate(line):
            if char == "E":  # start at the end so as to find fewer paths
                start.x = c
                start.y = r
            if char == "S":
                target = (c, r)
            row.append(get_char_index(char))

        grid.append(row)

    distances = [x for x in get_distance(grid, start.coords, targets=[target])]

    return str(min(x.steps for x in distances))


if __name__ == "__main__":
    print(main())
