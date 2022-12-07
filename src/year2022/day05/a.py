import sys

import utils
from injection import input_injection


def get_top_crates(_input: str, reverse: bool = False) -> str:
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

        crates = columns[from_][-qty:]
        columns[to_] += crates[::-1] if reverse else crates
        columns[from_] = columns[from_][:-qty]

    return str("".join(x[-1] for x in columns.values() if x))


@input_injection
def main(_input: str) -> str:
    return get_top_crates(_input, reverse=True)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
