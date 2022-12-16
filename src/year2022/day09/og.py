import sys

from injection import input_injection
from models import Coords


@input_injection
def part_1(_input: str) -> str:
    """
    Original solution was to just move the tail to where the head was previously
    """
    result: int = 0
    seen: set[tuple[int, int]] = set()

    head = Coords(name="head")
    tail = Coords(name="tail")

    for line in _input.splitlines():
        direction, steps = line.split()
        for _ in range(int(steps)):
            previous_position = head.coords
            if direction == "R":
                head.x += 1
            if direction == "L":
                head.x -= 1
            if direction == "U":
                head.y += 1
            if direction == "D":
                head.y -= 1

            dx = abs(tail.x - head.x)
            dy = abs(tail.y - head.y)
            if dx > 1 or dy > 1:
                tail.x, tail.y = previous_position

            seen.add(tail.coords)

    result = len(seen)

    return str(result)


if __name__ == "__main__":
    try:
        provided_input = sys.argv[1]
    except IndexError:
        provided_input = ""
    print(part_1(provided_input))
