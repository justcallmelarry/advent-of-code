import sys

from injection import input_injection
from year2022.day07.a import get_data


@input_injection
def main(_input: str) -> str:
    result: int = 0

    space_used, tree = get_data(_input)

    total_space = 70000000
    need_space = 30000000

    free_up = need_space - (total_space - space_used)

    possible_dirs = [v for v in tree.values() if v >= free_up]
    result = min(possible_dirs)

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
