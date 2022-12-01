import sys

import injection
import utils


@injection.input_injection
def main(_input: str, sample_input: bool = False) -> str:
    result: str | int = ""

    elves_input = _input.split("\n\n")
    elves = [sum(utils.ints(elf)) for elf in elves_input]

    result = max(elves)

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
