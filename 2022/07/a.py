import collections
import sys
from pathlib import Path

import utils
from injection import input_injection


def get_tree(_input: str) -> dict[Path, int]:
    tree: dict[Path, int] = collections.defaultdict(int)
    current_path = Path()

    for line in _input.splitlines():
        chunks = line.split()
        if chunks[1] == "cd":
            dirname = chunks[2]
            if dirname == "..":
                current_path = current_path.parent
            elif current_path:
                current_path = current_path / dirname
            else:
                current_path = Path(dirname)

        elif chunks[0].isnumeric():
            tree[current_path] += utils.positive_ints(line)[0]

    new_tree: dict[Path, int] = collections.defaultdict(int)
    for key, value in tree.items():
        new_tree.setdefault(key, 0)
        new_tree[key] += value

        while str(key) != "/":
            key = key.parent
            new_tree[key] += value

    return new_tree


@input_injection
def main(_input: str) -> str:
    result: int = 0

    tree = get_tree(_input)

    result = sum([v for v in tree.values() if v <= 100000])

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
