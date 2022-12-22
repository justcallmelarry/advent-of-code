from shapely.geometry import Polygon
from shapely.ops import clip_by_rect, unary_union

import utils
from injection import input_injection


@input_injection
def main(_input: str) -> str:
    test = _input.startswith("Sensor at x=2")
    target = 10 if test else 2000000

    shape = Polygon()
    min_x = 0
    max_x = 0

    for line in _input.splitlines():
        sx, sy, bx, by = utils.ints(line)
        md = abs(sx - bx) + abs(sy - by)

        min_x = min(min_x, sx - md)
        max_x = max(max_x, sx + md)

        shape = unary_union(
            [
                shape,
                Polygon(
                    [
                        (sx, sy + md),
                        (sx - md, sy),
                        (sx, sy - md),
                        (sx + md, sy),
                    ]
                ),
            ]
        )

    # cut out one row as rect and get the area
    subset_rectangle = clip_by_rect(shape, min_x, target, max_x, target + 1)
    return str(int(subset_rectangle.area))


if __name__ == "__main__":
    print(main())
