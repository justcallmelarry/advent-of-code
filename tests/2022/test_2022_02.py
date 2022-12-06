import importlib
import re
from typing import Literal

import pytest

yearday = re.sub("[^0-9]", "", str(__file__))

sample = """A Y
B X
C Z"""

@pytest.mark.parametrize(
    ("part_name", "expected", "provided_input"),
    [
        ("a", "15", sample),
        ("b", "12", sample),
        ("a", "11873", ""),
        ("b", "12014", ""),
    ],
)
def test_result(part_name: Literal["a", "b"], expected: str, provided_input: str) -> None:
    if expected == "CHANGEME":
        pytest.skip()
    mod = importlib.import_module(f"{yearday[:4]}.{str(yearday[-2:]).zfill(2)}.{part_name}")
    assert mod.main(provided_input=provided_input) == expected
