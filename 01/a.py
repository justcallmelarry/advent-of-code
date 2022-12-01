import os
import sys

import utils


def get_input(sample: bool = False) -> str:
    day = os.path.dirname(os.path.abspath(__file__)).rsplit("/", 1)[-1]
    if sample:
        return utils.get_sample(day=day)

    return utils.get_actual(day=int(day), year=2022)


def main(_input: str) -> str:
    result: str | int = ""
    elves = []

    current_elf = 0
    for i in _input.splitlines():
        if i:
            current_elf += int(i)
        else:
            elves.append(current_elf)
            current_elf = 0

    result = max(elves)

    return str(result)


if __name__ == "__main__":
    print(main(get_input(sample=True if "--sample" in sys.argv else False)))
