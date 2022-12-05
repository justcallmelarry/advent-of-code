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
        for i, value in enumerate(row[1::4], start=1):
            columns[i] += value.strip()

    for line in directions.splitlines():
        cmd = utils.positive_ints(line)
        from_ = cmd[1]
        to_ = cmd[2]
        qty = cmd[0]

        # better solution for large loops
        crate = columns[from_][-qty:]
        columns[to_] += crate[::-1]  # reverse the string
        columns[from_] = columns[from_][:-qty]

    return str("".join(x[-1] for x in columns.values() if x))


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
