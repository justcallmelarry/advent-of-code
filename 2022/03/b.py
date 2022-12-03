import string
import sys

from injection import input_injection

VALUES = "_" + string.ascii_lowercase + string.ascii_uppercase


def get_value(c: str) -> int:
    return VALUES.index(c)


@input_injection
def main(_input: str, sample_input: bool = False) -> str:
    result: int = 0

    lines = _input.splitlines()

    while lines:
        # reduce the lines 3 at a time to create a group
        group = [lines.pop() for _ in range(3)]

        # intersect the elves to get the common badge item
        e1, e2, e3 = (set(e) for e in group)
        for c in list(e1.intersection(e2).intersection(e3)):
            result += get_value(c)

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
