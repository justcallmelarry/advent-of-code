import collections
import sys

import utils
from injection import input_injection


def get_ribbon(l: int, w: int, h: int) -> int:
    smallest = sorted([l, w, h])[:2]
    return l * w * h + smallest[0] * 2 + smallest[1] * 2


@input_injection
def main(_input: str) -> str:
    result: int = 0

    for line in _input.splitlines():
        l, w, h = utils.positive_ints(line)
        result += get_ribbon(l, w, h)

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
