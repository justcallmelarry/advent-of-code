import importlib
import re
from typing import Literal

import pytest

yearday = re.sub("[^0-9]", "", str(__file__))


@pytest.mark.parametrize(
    ("part_name", "expected", "provided_input"),
    [
        ("a", "-3", ")())())"),
        ("a", "0", "(())"),
        ("a", "3", "(()(()("),
        ("a", "3", "))((((("),
        ("b", "1", ")"),
        ("b", "5", "()())"),
        ("a", "232", ""),
        ("b", "1783", ""),
    ],
)
def test_result(part_name: Literal["a", "b"], expected: str, provided_input: str) -> None:
    if expected == "CHANGEME":
        pytest.skip()
    mod = importlib.import_module(f"{yearday[:4]}.{str(yearday[-2:]).zfill(2)}.{part_name}")
    assert mod.main(provided_input=provided_input) == expected