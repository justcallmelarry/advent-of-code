import importlib
import re
from typing import Literal

import pytest

yearday = re.sub("[^0-9]", "", str(__file__))


@pytest.mark.parametrize(
    ("part_name", "expected", "sample"),
    [
        ("a", "CHANGEME", True),
        ("b", "CHANGEME", True),
        ("a", "CHANGEME", False),
        ("b", "CHANGEME", False),
    ],
)
def test_result(part_name: Literal["a", "b"], expected: str, sample: bool) -> None:
    if expected == "CHANGEME":
        pytest.skip()
    mod = importlib.import_module(f"{yearday[:4]}.{str(yearday[-2:]).zfill(2)}.{part_name}")
    assert mod.main(sample) == expected
