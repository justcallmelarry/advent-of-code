import collections

import utils
from injection import input_injection


@input_injection
def part_2(_input: str) -> str:
    """
    Originally i used a deque to rotate the sprite, which was a great and easy
    solution except that it still counted the trailing # on the previous line,
    giving some edge pieces filled that should not be.
    """

    sprite = collections.deque("###....................................."[::1])
    output = ""

    cycles = 1

    for line in _input.splitlines():
        add_x = 0
        match line.split():
            case ["noop"]:
                current_cycles = 1
            case ["addx", number]:
                current_cycles = 2
                add_x = int(number)

        for _ in range(current_cycles):
            output += utils.FILLED_CHAR if sprite[(cycles - 1) % 40] == "#" else " "

            if cycles % 40 == 0:
                output += "\n"

            cycles += 1

        sprite.rotate(add_x)

    return "\n" + output


if __name__ == "__main__":
    print(part_2())
