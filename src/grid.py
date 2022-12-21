from __future__ import annotations

import math
from collections import defaultdict
from typing import Any, Iterator

CoordsType = tuple[int, int]

_ADJACENT = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]


class OutOfBoundsErrror(Exception):
    def __init__(self, message: str, coords: CoordsType) -> None:
        self.message = message
        self.coords = coords
        super().__init__(message)


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

        self._data: defaultdict[CoordsType, Any] = defaultdict()

    def __getitem__(self, item: CoordsType) -> Any:
        return self._data[item]

    def __setitem__(self, item: CoordsType, value: Any) -> None:
        self.update(item, value)

    def get_neighbours(
        self,
        coords: CoordsType,
        include_diagonals: bool = False,
        include_out_of_bounds: bool = False,
    ) -> Iterator[CoordsType]:
        for direction in _ADJACENT:
            try:
                new_coords = self.move(coords, direction)
                if not include_diagonals and 0 not in new_coords:
                    continue
                yield new_coords
            except OutOfBoundsErrror as e:
                if include_out_of_bounds:
                    yield e.coords

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
        if not self.inbounds(coords):
            return

        self.x_min = min(coords[0], self.x_min)
        self.x_max = max(coords[0], self.x_max)
        self.y_min = min(coords[1], self.y_min)
        self.y_max = max(coords[1], self.y_max)


        self._data[coords] = fill

    def get_value(self, coords: CoordsType) -> Any:
        if not self.inbounds(coords):
            return math.inf
        return self._data.get(coords, self.default)

    def move(self, current_coords: CoordsType, movement: CoordsType) -> CoordsType:
        new_coords = (current_coords[0] + movement[0], current_coords[1] + movement[1])
        if not self.inbounds(new_coords):
            raise OutOfBoundsErrror("Out of bounds", coords=new_coords)
        return (current_coords[0] + movement[0], current_coords[1] + movement[1])

    def get_row_coords(self, row: int) -> list[CoordsType]:
        return [key for key in self._data.keys() if key[1] == row]

    def get_row_values(self, row: int) -> list:
        return [value for key, value in self._data.items() if key[1] == row]

    def get_col_coords(self, col: int) -> list[CoordsType]:
        return [key for key in self._data.keys() if key[0] == col]

    def get_col_values(self, col: int) -> list:
        return [value for key, value in self._data.items() if key[0] == col]

    def _get_relative_coords(self, coords: CoordsType) -> CoordsType:
        x, y = coords
        x += abs(self.x_min) if self.x_min <= 0 else -self.x_min
        y += abs(self.y_min) if self.y_min <= 0 else -self.y_min

        return (x, y)

    @property
    def output(self) -> str:
        maxsize = 200
        if any([self.abswidth > maxsize, self.absheight > maxsize]):
            return "too big to output"

        if not isinstance(self.default, (str, int)) and not len(str(self.default)) == 1:
            return "not outputtable"

        format_row_value = len(str(self.absheight)) + 1
        output: list[list[str]] = []

        for _ in range(self.absheight + 1):
            output.append([str(self.default)] * (self.abswidth + 1))

        for coords, value in self._data.items():
            rel_coords = self._get_relative_coords(coords)
            output[rel_coords[1]][rel_coords[0]] = str(value)

        return "\n".join([str(self.y_min + i).zfill(format_row_value) + " " + "".join(r) for i, r in enumerate(output)])


    @staticmethod
    def between(a: tuple[int, int], b: tuple[int, int], check: tuple[int, int]) -> bool:
        bl = (min(a[0], b[0]), min(a[1], b[1]))
        tr = (max(a[0], b[0]), max(a[1], b[1]))

        if not bl[0] <= check[0] <= tr[0]:
            return False
        if not bl[1] <= check[1] <= tr[1]:
            return False
        return True
