import sys

from injection import input_injection


@input_injection
def main(_input: str) -> str:
    result: int = 0

    values = {
        "(": 1,
        ")": -1,
    }

    floor = 0
    for i, char in enumerate(_input, start=1):
        floor += values[char]
        if floor == -1:
            result = i
            break

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
