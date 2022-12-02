import heapq
import sys

import injection
import utils


@injection.input_injection
def main(_input: str, sample_input: bool = False) -> str:
    result: int = 0

    elves_input = _input.split("\n\n")
    elves = [sum(utils.ints(elf)) for elf in elves_input]

    result = sum(heapq.nlargest(3, elves))

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
