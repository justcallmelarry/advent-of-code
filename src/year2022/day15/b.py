from shapely.geometry import Polygon
from shapely.ops import clip_by_rect, unary_union

import utils
from injection import input_injection


@input_injection
def main(_input: str) -> str:
    test = _input.startswith("Sensor at x=2")
    target = 20 if test else 4000000

    shape = Polygon()

    min_x = 0
    max_x = 0

    for line in _input.splitlines():
        sx, sy, bx, by = utils.ints(line)
        md = abs(sx - bx) + abs(sy - by)

        min_x = min(min_x, sx - md)
        max_x = min(max_x, sx + md)

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

    subset_rectangle = clip_by_rect(shape, min_x, 0, target, target)
    interior = subset_rectangle.interiors[0]
    x, y = tuple(map(round, interior.centroid.coords[:][0]))
    return str(x * 4000000 + y)


if __name__ == "__main__":
    print(main())
