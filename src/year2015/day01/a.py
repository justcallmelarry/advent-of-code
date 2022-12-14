import collections

from injection import input_injection


@input_injection
def main(_input: str) -> str:
    result: int = 0

    counter = collections.Counter(list(_input[::1]))
    result = 1 * counter["("] + -1 * counter[")"]

    return str(result)


if __name__ == "__main__":
    print(main())
