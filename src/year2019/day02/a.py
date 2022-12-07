import sys
from copy import deepcopy

import utils
from injection import input_injection


def run_intcode_input(int_list: list[int]) -> list[int]:
    output = deepcopy(int_list)
    pos = 0
    while True:
        opcode = output[pos]

        if opcode == 99:
            return output

        pos1 = output[pos + 1]
        pos2 = output[pos + 2]
        pos3 = output[pos + 3]

        if opcode == 1:
            output[pos3] = output[pos1] + output[pos2]

        if opcode == 2:
            output[pos3] = output[pos1] * output[pos2]

        pos += 4


@input_injection
def main(_input: str) -> str:
    int_list = utils.ints(_input)

    # set the parameters to recreate the crash
    int_list[1] = 12
    int_list[2] = 2

    result = run_intcode_input(int_list)

    return str(result[0])


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
