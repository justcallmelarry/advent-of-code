import string
import sys

from injection import input_injection

VALUES = "_" + string.ascii_lowercase + string.ascii_uppercase


def get_value(c: str) -> int:
    return VALUES.index(c)


@input_injection
def main(_input: str, sample_input: bool = False) -> str:
    result: int = 0

    for line in _input.splitlines():
        half_line = len(line) // 2
        compartment_a = set(line[:half_line])
        compartment_b = set(line[half_line:])
        for c in list(compartment_a.intersection(compartment_b)):
            result += get_value(c)

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
