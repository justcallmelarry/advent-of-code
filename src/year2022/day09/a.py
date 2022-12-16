
from injection import input_injection
from models import Coords


def move_towards(b: Coords, a: Coords) -> None:
    if a.x < b.x:
        b.x -= 1

    elif a.x > b.x:
        b.x += 1

    if a.y < b.y:
        b.y -= 1

    elif a.y > b.y:
        b.y += 1


def follow(a: Coords, b: Coords) -> None:
    """
    check if adjacent, move if not
    """
    dx = abs(b.x - a.x)
    dy = abs(b.y - a.y)

    if dx > 1 or dy > 1:
        move_towards(b, a)


def move_head(head, direction) -> None:
    if direction == "R":
        head.x += 1
    if direction == "L":
        head.x -= 1
    if direction == "U":
        head.y += 1
    if direction == "D":
        head.y -= 1


@input_injection
def main(_input: str) -> str:
    result: int = 0
    seen: set[tuple[int, int]] = set()

    head = Coords(name="head")
    tail = Coords(name="tail")

    for line in _input.splitlines():
        direction, steps = line.split()
        for _ in range(int(steps)):
            move_head(head, direction)
            follow(head, tail)
            seen.add(tail.coords)

    result = len(seen)

    return str(result)


if __name__ == "__main__":
    print(main())
