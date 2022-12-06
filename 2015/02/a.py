import collections
import sys

import utils
from injection import input_injection


def get_area(l: int, w: int, h: int) -> int:
    sides = [(l * w), (w * h), (h * l)]
    return 2 * sum(sides) + min(sides)


@input_injection
def main(_input: str) -> str:
    result: int = 0

    for line in _input.splitlines():
        l, w, h = utils.positive_ints(line)
        result += get_area(l, w, h)

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
