import collections

import utils
from injection import input_injection


@input_injection
def main(_input: str) -> str:
    result: int = 0

    # code here

    return str(result)


if __name__ == "__main__":
    print(main())
