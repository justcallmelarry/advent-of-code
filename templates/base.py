import collections
import os
import sys

import injection
import utils


@injection.input_injection
def main(_input: str, sample_input: bool = False) -> str:
    result: str | int = ""

    # code here

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
