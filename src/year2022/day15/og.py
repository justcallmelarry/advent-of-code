import collections

import utils
from grid import Sparse
from injection import input_injection
from models import Coords


class Signal(Coords):
    beacon_dist: int = 0


def add_seen(target: int, signal: Signal, seen: set[tuple[int, int]]) -> set[tuple[int, int]]:
    w, h = 0, signal.beacon_dist
    x, y = signal.coords
    if not y - signal.beacon_dist <= target <= y + signal.beacon_dist:
        return seen

    while h != -1:
        if target in (y + h, y - h):
            seen.update(
                [
                    (x + w, y + h),
                    (x - w, y - h),
                    (x - w, y + h),
                    (x + w, y - h),
                ]
            )
            for i in range(x - w, x + w):
                seen.update([(i, y + h), (i, y - h)])
        w += 1
        h -= 1

    return seen


@input_injection
def part_1(_input: str) -> str:
    """
    Original part 1 just prints all the diamonds and then calculates the target line without any bells of whistles
    """
    test = _input.startswith("Sensor at x=2")
    target = 10 if test else 2000000
    grid = Sparse(default=".")
    signals = []

    for line in _input.splitlines():
        sx, sy, bx, by = utils.ints(line)
        beacon_coords = (bx, by)
        signal = Signal(x=sx, y=sy)
        signal.beacon_dist = utils.manhattan_dist(signal.coords, beacon_coords)
        signals.append(signal)
        grid.update(signal.coords, "S")
        grid.update(beacon_coords, "B")

    seen: set[tuple[int, int]] = set()
    for signal in signals:
        add_seen(target, signal, seen)

    row_seen = set([s for s in seen if s[1] == target])
    row_other = grid.get_row_coords(target)

    result = len(row_seen) - len(row_other)

    return str(result)


SeenType = tuple[int, int]


class FastForward(Exception):
    pass


def get_ranges(target: int, signal: Signal, seen_ranges: collections.defaultdict[int, set[SeenType]]) -> None:
    w, h = 0, signal.beacon_dist
    x, y = signal.coords
    while h >= -signal.beacon_dist:
        try:
            y_value = y + h
            if not 0 <= y_value <= target:
                raise FastForward

            low_x = x - w
            high_x = x + w
            if (low_x, high_x) in ((0, 0), (target, target)):
                raise FastForward

            seen = seen_ranges.get(y_value) or set()

            for r in list(seen):
                check = utils.overlaps([low_x, high_x], [*r])
                if len(check) != 0:
                    seen.remove(r)
                    low_x = min(low_x, r[0])
                    high_x = max(high_x, r[1])

            seen.add((low_x, high_x))

            seen_ranges[y_value] = seen
        except FastForward:
            pass

        w += 1 if h > 0 else -1
        h -= 1


@input_injection
def part_2(_input: str) -> str:
    """
    Original part 2 solution takes the approach to look for all ranges covered on a row,
    then iterates over them to find out wher a gap exists in the row
    """
    test = _input.startswith("Sensor at x=2")
    target = 20 if test else 4000000

    grid = Sparse(width=target, height=target, default=".")
    signals = []

    for line in _input.splitlines():
        sx, sy, bx, by = utils.ints(line)
        beacon_coords = (bx, by)
        signal = Signal(x=sx, y=sy)
        signal.beacon_dist = utils.manhattan_dist(signal.coords, beacon_coords)
        signals.append(signal)
        grid.update(signal.coords, "S")
        grid.update(beacon_coords, "B")

    seen_ranges: collections.defaultdict[int, set[SeenType]] = collections.defaultdict()
    for signal in signals:
        get_ranges(target, signal, seen_ranges)

    if test:
        for debug_y, seen in seen_ranges.items():
            for debug_x_range in seen:
                for debug_x in range(debug_x_range[0], debug_x_range[1] + 1):
                    debug_coords = (debug_x, debug_y)
                    if grid.get_value(debug_coords) == ".":
                        grid.update(debug_coords, "#")

        print(grid.output)

    for y in range(grid.y_min, grid.y_max + 1):
        seen = seen_ranges.get(y) or set()
        x = 0
        while x <= target:
            try:
                for r in seen:
                    if r[0] <= x <= r[1]:
                        x = min(r[1], target)
                        raise FastForward
            except FastForward:
                x += 1
                continue

            return str(x * 4000000 + y)

    return "0"


if __name__ == "__main__":
    print(part_1())
    print(part_2())
