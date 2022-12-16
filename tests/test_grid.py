from grid import Sparse

output = """-1 .#.
00 #.#
01 .#."""


def test_relative_coords() -> None:
    grid = Sparse(default=".")

    coords_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for coords in coords_list:
        grid.update(coords, "#")

    assert grid._get_relative_coords((-1, 0)) == (0, 1)


def test_output() -> None:
    grid = Sparse(default=".")

    coords_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for coords in coords_list:
        grid.update(coords, "#")

    assert grid.output == output


def test_between() -> None:
    grid = Sparse(default=".")

    assert grid.between((0, 0), (0, 2), (0, 1))
