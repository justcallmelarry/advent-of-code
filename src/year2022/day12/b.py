from injection import input_injection
from models import Coords
from year2022.day12.a import get_char_index, get_distance


@input_injection
def main(_input: str) -> str:
    start = Coords(name="start")
    grid: list[list[int]] = []
    targets = []

    for r, line in enumerate(_input.splitlines()):
        row: list[int] = []

        for c, char in enumerate(line):
            if char == "E":
                start.x = c
                start.y = r
            if char in ("S", "a"):
                target = (c, r)
                targets.append(target)

            row.append(get_char_index(char))

        grid.append(row)

    distances = [x for x in get_distance(grid, start.coords, targets=targets)]

    return str(min(x.steps for x in distances))


if __name__ == "__main__":
    print(main())
