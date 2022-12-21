import collections

import utils
from injection import input_injection
from year2022.day18.a import get_neighbours, get_surface

CoordType = tuple[int, int, int]


@input_injection
def main(_input: str) -> str:
    lava_drop: list[CoordType] = [tuple(utils.ints(line)) for line in _input.splitlines()]  # type: ignore
    min_x, max_x = utils.min_max([x[0] for x in lava_drop])
    min_y, max_y = utils.min_max([x[1] for x in lava_drop])
    min_z, max_z = utils.min_max([x[2] for x in lava_drop])

    # create empty space that is just bigger than entire lava drop
    # in order to allow crawler to pass around the edges
    empty_space = set(
        (x, y, z)
        for x in range(min_x - 1, max_x + 2)
        for y in range(min_y - 1, max_y + 2)
        for z in range(min_z - 1, max_z + 2)
    )
    # then remove all the lava drop cubes
    empty_space -= set(lava_drop)

    def oob(coords: CoordType) -> bool:
        """
        simple out of bounds check
        """
        if not min_x - 1 <= coords[0] <= max_x + 1:
            return True
        if not min_y - 1 <= coords[1] <= max_y + 1:
            return True
        if not min_z - 1 <= coords[2] <= max_z + 1:
            return True
        return False

    q = collections.deque([(min_x, min_y, min_z)])
    seen = set((min_x, min_y, min_z))
    while q:
        coords = q.popleft()

        if coords in lava_drop:
            continue

        for n in get_neighbours(coords):
            if n in seen or oob(n):
                continue

            seen.add(n)
            q.append(n)

    # remove the spaces discovered by crawler
    empty_space -= seen

    # use the surface area of part 1 and subtract the surface area of the insides
    result = get_surface(lava_drop) - get_surface(list(empty_space))

    return str(result)


if __name__ == "__main__":
    print(main())
