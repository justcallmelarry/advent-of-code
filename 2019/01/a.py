import math
import sys

import injection
import utils


def get_fuel(x: int) -> int:
    return math.floor(x / 3) - 2


@injection.input_injection
def main(_input: str, sample_input: bool = False) -> str:
    result: int = 0

    result = sum(get_fuel(x) for x in utils.ints(_input))

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
