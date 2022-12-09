
import utils
from injection import input_injection


def get_elves(_input: str) -> list[int]:
    elves_input = _input.split("\n\n")
    elves = [sum(utils.ints(elf)) for elf in elves_input]
    return elves


@input_injection
def main(_input: str) -> str:
    result: int = 0

    elves = get_elves(_input)
    result = max(elves)

    return str(result)


if __name__ == "__main__":
    print(main())
