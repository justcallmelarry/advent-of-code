
from injection import input_injection


def get_directional_value(direction: list[int], tree: int) -> int:
    if not direction:
        return 0
    for i, view in enumerate(direction, start=1):
        if tree <= view:
            return i
    return i


@input_injection
def main(_input: str) -> str:
    grid: list[list[int]] = []

    for line in _input.splitlines():
        grid.append([int(c) for c in line])

    hiscore = 0

    for r, row in enumerate(grid):
        for c, tree in enumerate(row):
            scenic_score: int = 1
            score = []

            direction_n = [v[c] for v in grid[:r]]
            score.append(get_directional_value(direction_n[::-1], tree))

            direction_w = [v for v in row[:c]]
            score.append(get_directional_value(direction_w[::-1], tree))

            direction_s = [v[c] for v in grid[r + 1 :]]
            score.append(get_directional_value(direction_s, tree))

            direction_e = [v for v in row[c + 1 :]]
            score.append(get_directional_value(direction_e, tree))

            for s in score:
                scenic_score *= s

            if scenic_score > hiscore:
                hiscore = scenic_score

    return str(hiscore)


if __name__ == "__main__":
    print(main())
