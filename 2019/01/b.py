import math
import sys

import utils
from injection import input_injection


def get_fuel(x: int) -> int:
    fuel = math.floor(x / 3) - 2
    if fuel < 0:
        return 0
    return fuel


@input_injection
def main(_input: str) -> str:
    result: int = 0

    for x in utils.ints(_input):
        fuel = get_fuel(x)
        result += fuel
        while fuel:
            fuel = get_fuel(fuel)
            result += fuel

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
