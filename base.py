import collections
import os
import sys

import utils


def get_input(sample: bool = False) -> str:
    year, day = os.path.dirname(os.path.abspath(__file__)).rsplit("/", 2)[-2:]
    if sample:
        return utils.get_sample(day=int(day), year=int(year))

    return utils.get_actual(day=int(day), year=int(year))


def main(_input: str) -> str:
    result: str | int = ""

    # code here

    return str(result)


if __name__ == "__main__":
    print(main(get_input(sample=True if "--sample" in sys.argv else False)))
