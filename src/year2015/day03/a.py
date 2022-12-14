from injection import input_injection
from models import Coords


def get_coords(_input: str, start: int = 0, steps: int = 1) -> set[str]:
    santa = Coords(name="santa")
    coords = set()
    coords.add(santa.current_pos)
    for direction in _input[start::steps]:
        if direction == "<":
            santa.x -= 1
        if direction == ">":
            santa.x += 1
        if direction == "v":
            santa.y -= 1
        if direction == "^":
            santa.y += 1
        coords.add(santa.current_pos)

    return coords


@input_injection
def main(_input: str) -> str:
    coords = get_coords(_input)

    return str(len(coords))


if __name__ == "__main__":
    print(main())
