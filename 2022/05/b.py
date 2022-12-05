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

    base_rows.reverse()
    for row in base_rows:
        for i, box in enumerate(row[1::4], start=1):
            columns[i] += re.sub("[^A-Z]", "", box)

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
