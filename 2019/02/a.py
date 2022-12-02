import sys

import utils
from injection import input_injection


@input_injection
def main(_input: str, sample_input: bool = False) -> str:
    result: int = 0

    int_list = utils.ints(_input)

    # set the parameters to recreate the crash
    int_list[1] = 12
    int_list[2] = 2

    pos = 0
    while True:
        opcode = int_list[pos]

        if opcode == 99:
            break

        pos1 = int_list[pos + 1]
        pos2 = int_list[pos + 2]
        pos3 = int_list[pos + 3]

        if opcode == 1:
            int_list[pos3] = int_list[pos1] + int_list[pos2]

        if opcode == 2:
            int_list[pos3] = int_list[pos1] * int_list[pos2]

        pos += 4

    result = int_list[0]

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
