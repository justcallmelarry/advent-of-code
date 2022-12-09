
from injection import input_injection
from year2022.day06.a import get_signal_message_char


@input_injection
def main(_input: str) -> str:
    result = get_signal_message_char(_input, 14)

    return str(result)


if __name__ == "__main__":
    print(main())
