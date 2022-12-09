import string

import utils
from injection import input_injection

VALUES = "_" + string.ascii_lowercase + string.ascii_uppercase


def get_value(c: str) -> int:
    return VALUES.index(c)


@input_injection
def main(_input: str) -> str:
    result: int = 0

    for line in _input.splitlines():
        compartment_a, compartment_b = (set(x) for x in utils.split_string(line))
        for c in list(compartment_a.intersection(compartment_b)):
            result += get_value(c)

    return str(result)


if __name__ == "__main__":
    print(main())
