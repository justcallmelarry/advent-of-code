import collections
import os
import sys

import utils
from injection import input_injection


@input_injection
def main(_input: str, sample_input: bool = False) -> str:
    result: int = 0

    # code here

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
