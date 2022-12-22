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
def main(_input: str) -> str:
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


if __name__ == "__main__":
    print(main())
