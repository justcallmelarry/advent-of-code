import importlib
import re
from typing import Literal

import pytest

from infra import get_mod_path

yearday = re.sub("[^0-9]", "", str(__file__))


@pytest.mark.parametrize(
    ("part_name", "expected", "provided_input"),
    [
        ("a", "31", "Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi"),
        ("a", "27", "SabcdefghijklmnopqrstuvwxyzE"),
        ("a", "27", "Sabc\ngfed\nhijk\nonml\npqrs\nwvut\nxyzE"),
        ("b", "29", "Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi"),
        ("a", "440", ""),
        ("b", "439", ""),
    ],
)
def test_result(part_name: Literal["a", "b"], expected: str, provided_input: str) -> None:
    if expected == "CHANGEME":
        pytest.skip()
    mod_path = get_mod_path(int(yearday[:4]), int(yearday[-2:]), part_name)
    mod = importlib.import_module(mod_path)
    assert mod.main(provided_input=provided_input) == expected
