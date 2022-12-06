import importlib
import re
from typing import Literal

import pytest

yearday = re.sub("[^0-9]", "", str(__file__))

sample = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

@pytest.mark.parametrize(
    ("part_name", "expected", "provided_input"),
    [
        ("a", "CMZ", sample),
        ("b", "MCD", sample),
        ("a", "RFFFWBPNS", ""),
        ("b", "CQQBBJFCS", ""),
    ],
)
def test_result(part_name: Literal["a", "b"], expected: str, provided_input: str) -> None:
    if expected == "CHANGEME":
        pytest.skip()
    mod = importlib.import_module(f"{yearday[:4]}.{str(yearday[-2:]).zfill(2)}.{part_name}")
    assert mod.main(provided_input=provided_input) == expected
