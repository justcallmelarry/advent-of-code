
import utils
from injection import input_injection
from year2019.day01.a import get_fuel


@input_injection
def main(_input: str) -> str:
    result: int = 0

    for x in utils.ints(_input):
        fuel = get_fuel(x)
        result += fuel
        while fuel:
            fuel = get_fuel(fuel)
            result += fuel

    return str(result)


if __name__ == "__main__":
    print(main())
