import collections
import os
import sys

import utils
from injection import input_injection


def run_input(list_: list[int]) -> None:
    pos = 0
    while True:
        opcode = list_[pos]

        if opcode == 99:
            return

        pos1 = list_[pos + 1]
        pos2 = list_[pos + 2]
        pos3 = list_[pos + 3]

        if opcode == 1:
            list_[pos3] = list_[pos1] + list_[pos2]

        if opcode == 2:
            list_[pos3] = list_[pos1] * list_[pos2]

        pos += 4


@input_injection
def main(_input: str, sample_input: bool = False) -> str:
    int_list = utils.ints(_input)

    target = 19690720

    for x in range(100):
        for y in range(100):
            solution = 0

            new_list = int_list.copy()
            new_list[1] = x
            new_list[2] = y

            run_input(new_list)

            solution = new_list[0]

            if solution == target:
                break
        if solution == target:
            break

    return f"{x}{y}"


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
