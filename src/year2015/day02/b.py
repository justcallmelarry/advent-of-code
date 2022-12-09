
import utils
from injection import input_injection


def get_ribbon(length: int, width: int, height: int) -> int:
    smallest = sorted([length, width, height])[:2]
    return length * width * height + smallest[0] * 2 + smallest[1] * 2


@input_injection
def main(_input: str) -> str:
    result: int = 0

    for line in _input.splitlines():
        length, width, height = utils.positive_ints(line)
        result += get_ribbon(length, width, height)

    return str(result)


if __name__ == "__main__":
    print(main())
