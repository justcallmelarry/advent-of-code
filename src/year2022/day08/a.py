
from injection import input_injection


@input_injection
def main(_input: str) -> str:
    result: int = 0

    grid: list[list[int]] = []

    for line in _input.splitlines():
        grid.append([int(c) for c in line])

    for r, row in enumerate(grid):
        for c, tree in enumerate(row):
            if any(
                [
                    all(tree > v for v in row[:c]),
                    all(tree > v for v in row[c + 1 :]),
                    all(tree > v[c] for v in grid[:r]),
                    all(tree > v[c] for v in grid[r + 1 :]),
                ]
            ):
                result += 1

    return str(result)


if __name__ == "__main__":
    print(main())
