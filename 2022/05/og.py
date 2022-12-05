import re
import sys
from itertools import zip_longest

import utils
from injection import input_injection


@input_injection
def part_1(_input: str, sample_input: bool = False) -> str:
    base, directions = _input.split("\n\n")
    base_rows = base.splitlines()
    columns = {i: "" for i in utils.positive_ints(base_rows.pop(-1))}

    for row in base_rows:
        step = 3
        current_col = 1
        while len(row) >= step:
            crate = row[:3]
            columns[current_col] = re.sub("[^A-Z]", "", crate) + columns[current_col]

            row = row[3:]
            if len(row) >= 4:
                row = row[1:]
            current_col += 1

    for line in directions.splitlines():
        cmd = utils.positive_ints(line)

        for _ in range(cmd[0]):
            crate = columns[cmd[1]][-1:]
            columns[cmd[2]] += crate
            columns[cmd[1]] = columns[cmd[1]][:-1]

    return str("".join(x[-1] for x in columns.values() if x))


@input_injection
def part_2(_input: str, sample_input: bool = False) -> str:
    base, directions = _input.split("\n\n")
    base_rows = base.splitlines()
    columns = {i: "" for i in utils.positive_ints(base_rows.pop(-1))}

    for row in base_rows:
        step = 3
        current_col = 1
        while len(row) >= step:
            crate = row[:3]
            columns[current_col] = re.sub("[^A-Z]", "", crate) + columns[current_col]

            row = row[3:]
            if len(row) >= 4:
                row = row[1:]
            current_col += 1

    for line in directions.splitlines():
        cmd = utils.positive_ints(line)

        crate = columns[cmd[1]][-cmd[0] :]
        columns[cmd[2]] += crate
        columns[cmd[1]] = columns[cmd[1]][: -cmd[0]]

    return str("".join(x[-1] for x in columns.values() if x))


def print_columns(columns: dict) -> None:
    """
    not really used, but fun mostly for visualization
    """
    cols = []
    base = " ".join(str(c) for c in columns.keys())
    for t in zip_longest(*columns.values(), fillvalue=" "):
        cols.append(" ".join(t))
    cols.reverse()
    stacks = "\n".join(cols)
    print(f"{stacks}\n{base}\n")


if __name__ == "__main__":
    print(part_1(True if "--sample" in sys.argv else False))
    print(part_2(True if "--sample" in sys.argv else False))
