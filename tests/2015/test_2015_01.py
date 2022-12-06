import importlib
import re
from typing import Literal

import pytest

yearday = re.sub("[^0-9]", "", str(__file__))


@pytest.mark.parametrize(
    ("part_name", "expected", "sample", "provided_input"),
    [
        ("a", "-3", True, ""),
        ("a", "0", True, "(())"),
        ("a", "3", True, "(()(()("),
        ("a", "3", True, "))((((("),
        ("b", "1", True, ""),
        ("b", "1", True, ")"),
        ("b", "5", True, "()())"),
        ("a", "232", False, ""),
        ("b", "1783", False, ""),
    ],
)
def test_result(part_name: Literal["a", "b"], expected: str, sample: bool, provided_input: str) -> None:
    if expected == "CHANGEME":
        pytest.skip()
    mod = importlib.import_module(f"{yearday[:4]}.{str(yearday[-2:]).zfill(2)}.{part_name}")
    assert mod.main(sample=sample, provided_input=provided_input) == expected
