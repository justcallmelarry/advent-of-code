import collections
import sys

import utils
from injection import input_injection


@input_injection
def main(_input: str) -> str:
    result: int = 0

    # code here

    return str(result)


if __name__ == "__main__":
    try:
        provided_input = sys.argv[1]
    except IndexError:
        provided_input = ""
    print(main())
