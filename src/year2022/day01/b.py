import heapq

from injection import input_injection
from year2022.day01.a import get_elves


@input_injection
def main(_input: str) -> str:
    result: int = 0

    elves = get_elves(_input)

    result = sum(heapq.nlargest(3, elves))

    return str(result)


if __name__ == "__main__":
    print(main())
