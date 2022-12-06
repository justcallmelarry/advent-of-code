import importlib
import re
from typing import Literal

import pytest

yearday = re.sub("[^0-9]", "", str(__file__))


@pytest.mark.parametrize(
    ("part_name", "expected", "sample", "provided_input"),
    [
        ("a", "58", True, ""),
        ("b", "34", True, ""),
        ("a", "43", True, "1x1x10"),
        ("b", "14", True, "1x1x10"),
        ("a", "1588178", False, ""),
        ("b", "3783758", False, ""),
    ],
)
def test_result(part_name: Literal["a", "b"], expected: str, sample: bool, provided_input: str) -> None:
    if expected == "CHANGEME":
        pytest.skip()
    mod = importlib.import_module(f"{yearday[:4]}.{str(yearday[-2:]).zfill(2)}.{part_name}")
    assert mod.main(sample=sample, provided_input=provided_input) == expected
