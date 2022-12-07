import sys

from injection import input_injection
from year2022.day05.a import get_top_crates


@input_injection
def main(_input: str) -> str:
    return get_top_crates(_input)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
