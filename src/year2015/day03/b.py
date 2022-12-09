
from injection import input_injection
from year2015.day03.a import get_coords


@input_injection
def main(_input: str) -> str:
    santa_coords = get_coords(_input, steps=2)
    robot_coords = get_coords(_input, start=1, steps=2)
    return str(len(santa_coords | robot_coords))


if __name__ == "__main__":
    print(main())
