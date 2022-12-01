import heapq
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

    elves_input = _input.split("\n\n")
    elves = []
    for elf in elves_input:
        elves.append(sum([int(i) for i in elf.splitlines()]))

    result = sum(heapq.nlargest(3, elves))

    return str(result)


if __name__ == "__main__":
    print(main(get_input(sample=True if "--sample" in sys.argv else False)))
