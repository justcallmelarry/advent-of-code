import importlib
import re
from typing import Literal

import pytest

from infra import get_mod_path

yearday = re.sub("[^0-9]", "", str(__file__))


@pytest.mark.parametrize(
    ("part_name", "expected", "provided_input"),
    [
        ("a", "13", "R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2"),
        ("b", "36", "R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20"),
        ("a", "6354", ""),
        ("b", "2651", ""),
    ],
)
def test_result(part_name: Literal["a", "b"], expected: str, provided_input: str) -> None:
    if expected == "CHANGEME":
        pytest.skip()
    mod_path = get_mod_path(int(yearday[:4]), int(yearday[-2:]), part_name)
    mod = importlib.import_module(mod_path)
    assert mod.main(provided_input=provided_input) == expected
