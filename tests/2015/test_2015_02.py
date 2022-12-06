import importlib
import re
from typing import Literal

import pytest

yearday = re.sub("[^0-9]", "", str(__file__))


@pytest.mark.parametrize(
    ("part_name", "expected", "provided_input"),
    [
        ("a", "58", "2x3x4"),
        ("b", "34", "2x3x4"),
        ("a", "43", "1x1x10"),
        ("b", "14", "1x1x10"),
        ("a", "1588178", ""),
        ("b", "3783758", ""),
    ],
)
def test_result(part_name: Literal["a", "b"], expected: str, provided_input: str) -> None:
    if expected == "CHANGEME":
        pytest.skip()
    mod = importlib.import_module(f"{yearday[:4]}.{str(yearday[-2:]).zfill(2)}.{part_name}")
    assert mod.main(provided_input=provided_input) == expected
