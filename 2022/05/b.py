import collections
import re
import sys

import utils
from injection import input_injection


@input_injection
def main(_input: str, sample_input: bool = False) -> str:
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
        from_ = cmd[1]
        to_ = cmd[2]
        qty = cmd[0]

        crates = columns[from_][-qty:]
        columns[to_] += crates
        columns[from_] = columns[from_][:-qty]

    return str("".join(x[-1] for x in columns.values() if x))


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
