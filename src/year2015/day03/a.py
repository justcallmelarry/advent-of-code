import sys

from injection import input_injection


def get_coords(_input: str, start: int = 0, steps: int = 1) -> set[str]:
    x,y = 0,0
    coords = set(["0,0"])
    for direction in _input[start::steps]:
        match direction:
            case "<":
                x -= 1
            case ">":
                x += 1
            case "v":
                y -= 1
            case "^":
                y += 1
        coords.add(f"{x},{y}")

    return coords


@input_injection
def main(_input: str) -> str:
    coords = get_coords(_input)

    return str(len(coords))


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
