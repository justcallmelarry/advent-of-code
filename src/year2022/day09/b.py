
from injection import input_injection
from models import Coords
from year2022.day09.a import Coords, follow, move_head


@input_injection
def main(_input: str) -> str:
    result: int = 0
    seen: set[tuple[int, int]] = set()

    head = Coords(name="head")
    tail = Coords(name="tail")
    snake = [head]
    for i in range(8):
        snake.append(Coords(name=f"bodypart-{i + 1}"))
    snake.append(tail)

    for line in _input.splitlines():
        direction, steps = line.split()
        for _ in range(int(steps)):
            move_head(head, direction)

            for i in range(len(snake) - 1):
                follow(snake[i], snake[i + 1])

            seen.add(tail.current_pos)

    result = len(seen)

    return str(result)


if __name__ == "__main__":
    print(main())
