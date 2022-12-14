from __future__ import annotations

import math
from collections import defaultdict
from typing import Any

CoordsType = tuple[int, int]


class Grid:
    """
    If you really want to implement a 2d list grid
    """

    def __init__(self, height: int, width: int, fill: Any = None) -> None:
        self.height = height
        self.width = width
        self._data = self._make_grid([height, width], fill=fill)
        self.inf = math.inf

    def __getitem__(self, item: int) -> Any:
        return self._data[item]

    def _make_grid(self, dimensions: list[int], fill: Any = None) -> list:
        "Returns a grid such that 'dimensions' is juuust out of bounds."
        if len(dimensions) == 1:
            return [fill for _ in range(dimensions[0])]
        next_down = self._make_grid(dimensions[1:], fill=fill)
        return [list(next_down) for _ in range(dimensions[0])]

    def inbounds(self, coords: CoordsType) -> bool:
        return all(
            [
                coords[0] >= 0,
                coords[1] <= self.height - 1,
                coords[1] >= 0,
                coords[0] <= self.width - 1,
            ]
        )

    def get_value(self, coords: CoordsType) -> Any:
        if not self.inbounds(coords):
            return math.inf
        return self._data[coords[1]][coords[0]]

    @property
    def output(self) -> str:
        output = ""
        for row in self._data:
            output += "".join(x if x is not None else "" for x in row)
            output += "\n"

        return output

    def update(self, coords: CoordsType, fill: Any) -> None:
        self._data[coords[1]][coords[0]] = fill

    @classmethod
    def from_matrix(cls, matrix: list[list[Any]]) -> Grid:
        grid = Grid(height=len(matrix), width=len(matrix[0]))
        grid._data = matrix
        return grid


class Sparse:
    """
    Beginning implementation of a sparse grid
    By default unbound, but can be set to bound by providing size
    """

    def __init__(
        self,
        default: Any = None,
        height: int = 0,
        width: int = 0,
        zero_position: tuple[int, int] = (0, 0),
    ) -> None:
        self.default = default
        self.inf = math.inf

        self.x_max = width
        self.x_min = 0
        self.y_max = height
        self.y_min = 0

        self.bound = set()
        if height:
            self.bound.add("y")
        if width:
            self.bound.add("x")

        self.zero_position = zero_position
        self._data: defaultdict[tuple[int, int], Any] = defaultdict()

    def __getitem__(self, item: tuple[int, int]) -> Any:
        return self._data[item]

    def __setitem__(self, item: tuple[int, int], value: Any) -> None:
        self.update(item, value)

    @property
    def absheight(self) -> int:
        return abs(self.y_max - self.y_min)

    @property
    def abswidth(self) -> int:
        return abs(self.x_max - self.x_min)

    def inbounds(self, coords: CoordsType) -> bool:
        checks = []

        if "x" in self.bound:
            checks.append(coords[0] >= 0)
            checks.append(coords[0] <= self.x_max - 1)

        if "y" in self.bound:
            checks.append(coords[1] <= self.y_max - 1)
            checks.append(coords[1] >= 0)

        if not checks:
            return True

        return all(checks)

    def update(self, coords: CoordsType, fill: Any) -> None:
        self.x_min = min(coords[0], self.x_min)
        self.x_max = max(coords[0], self.x_max)
        self.y_min = min(coords[1], self.y_min)
        self.y_max = max(coords[1], self.y_max)

        self._data[coords] = fill

    def get_value(self, coords: CoordsType) -> Any:
        if not self.inbounds(coords):
            return math.inf
        return self._data.get(coords, self.default)
