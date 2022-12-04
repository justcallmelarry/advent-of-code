import collections
import sys

import utils
from injection import input_injection


@input_injection
def main(_input: str, sample_input: bool = False) -> str:
    result: int = 0

    for line in _input.splitlines():
        e1 = utils.positive_ints(line.split(",")[0])
        e2 = utils.positive_ints(line.split(",")[1])

        if any([e2[0] <= i <= e2[1] for i in e1]):
            result += 1
        elif any([e1[0] <= i <= e1[1] for i in e2]):
            result += 1

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
