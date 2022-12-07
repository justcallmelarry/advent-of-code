import sys

import utils
from injection import input_injection
from year2019.day02.a import run_intcode_input


@input_injection
def main(_input: str) -> str:
    int_list = utils.ints(_input)

    target = 19690720

    for x in range(100):
        for y in range(100):
            new_list = int_list.copy()
            new_list[1] = x
            new_list[2] = y

            solution = run_intcode_input(new_list)

            if solution[0] == target:
                break

        if solution[0] == target:
            break

    return f"{x}{y}"


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
