import importlib
import re
from typing import Literal

import pytest

from infra import get_mod_path

yearday = re.sub("[^0-9]", "", str(__file__))

sample = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


@pytest.mark.parametrize(
    ("part_name", "expected", "provided_input"),
    [
        ("a", "24000", sample),
        ("b", "45000", sample),
        ("a", "69883", ""),
        ("b", "207576", ""),
    ],
)
def test_result(part_name: Literal["a", "b"], expected: str, provided_input: str) -> None:
    if expected == "CHANGEME":
        pytest.skip()
    mod_path = get_mod_path(int(yearday[:4]), int(yearday[-2:]), part_name)
    mod = importlib.import_module(mod_path)
    assert mod.main(provided_input=provided_input) == expected
