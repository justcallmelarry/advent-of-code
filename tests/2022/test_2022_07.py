import importlib
import re
from typing import Literal

import pytest

yearday = re.sub("[^0-9]", "", str(__file__))

sample = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

own_sample="""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
dir e
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
$ cd ..
$ cd e
$ ls
100001 i"""


@pytest.mark.parametrize(
    ("part_name", "expected", "provided_input"),
    [
        ("a", "95437", sample),
        ("b", "24933642", sample),
        ("a", "95437", own_sample),
        ("b", "24933642", own_sample),
        ("a", "1667443", ""),
        ("b", "8998590", ""),
    ],
)
def test_result(part_name: Literal["a", "b"], expected: str, provided_input: str) -> None:
    if expected == "CHANGEME":
        pytest.skip()
    mod = importlib.import_module(f"{yearday[:4]}.{str(yearday[-2:]).zfill(2)}.{part_name}")
    assert mod.main(provided_input=provided_input) == expected
