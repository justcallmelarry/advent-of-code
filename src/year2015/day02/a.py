
import utils
from injection import input_injection


def get_area(length: int, width: int, height: int) -> int:
    sides = [(length * width), (width * height), (height * length)]
    return 2 * sum(sides) + min(sides)


@input_injection
def main(_input: str) -> str:
    result: int = 0

    for line in _input.splitlines():
        length, width, height = utils.positive_ints(line)
        result += get_area(length, width, height)

    return str(result)


if __name__ == "__main__":
    print(main())
