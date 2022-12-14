
from injection import input_injection


def get_signal_message_char(_input: str, size: int) -> int:
    result = 0
    for i in range(len(_input)):
        split = _input[i : i + size]
        if len(set(split)) == size:
            result = i + size
            break

    return result


@input_injection
def main(_input: str) -> str:
    result = get_signal_message_char(_input, 4)
    return str(result)


if __name__ == "__main__":
    print(main())
