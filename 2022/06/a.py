import sys

from injection import input_injection


@input_injection
def main(_input: str, sample_input: bool = False) -> str:
    result = 0
    size = 4

    for i in range(len(_input)):
        split = _input[i : i + size]
        if len(set(split)) == size:
            result = i + size
            break

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
