import collections
import sys
from pathlib import Path

import utils
from injection import input_injection


def get_data(_input: str) -> tuple[int, dict[Path, int]]:
    tree: dict[Path, int] = collections.defaultdict(int)
    current_path = Path()

    for line in _input.splitlines():
        chunks = line.split()

        match chunks:
            case ["$", "cd", "/"]:
                current_path = Path("/")
            case ["$", "cd"]:
                # this never happens in the input, but you never know
                current_path = Path("/")
            case ["$", "cd", ".."]:
                current_path = current_path.parent
            case ["$", "cd", dirname]:
                current_path = current_path / dirname
            case [file_size, _]:
                if file_size not in ("$", "dir"):
                    tree[current_path] += int(file_size)

    new_tree: dict[Path, int] = collections.defaultdict(int)
    for key, value in tree.items():
        new_tree.setdefault(key, 0)
        new_tree[key] += value

        while str(key) != "/":
            key = key.parent
            new_tree[key] += value

    return sum(tree.values()), new_tree


@input_injection
def main(_input: str) -> str:
    result: int = 0

    space_used, tree = get_data(_input)

    total_space = 70000000
    need_space = 30000000

    free_up = need_space - (total_space - space_used)

    possible_dirs = [v for v in tree.values() if v >= free_up]
    result = min(possible_dirs)

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
