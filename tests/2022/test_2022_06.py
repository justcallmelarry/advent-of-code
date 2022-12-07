import importlib
import re
from typing import Literal

import pytest

from infra import get_mod_path

yearday = re.sub("[^0-9]", "", str(__file__))


@pytest.mark.parametrize(
    ("part_name", "expected", "provided_input"),
    [
        ("a", "7", "mjqjpqmgbljsphdztnvjfqwrcgsmlb"),
        ("a", "5", "bvwbjplbgvbhsrlpgdmjqwftvncz"),
        ("a", "6", "nppdvjthqldpwncqszvftbrmjlhg"),
        ("a", "10", "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"),
        ("a", "11", "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"),
        ("b", "19", "mjqjpqmgbljsphdztnvjfqwrcgsmlb"),
        ("b", "23", "bvwbjplbgvbhsrlpgdmjqwftvncz"),
        ("b", "23", "nppdvjthqldpwncqszvftbrmjlhg"),
        ("b", "29", "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"),
        ("b", "26", "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"),
        ("a", "1647", ""),
        ("b", "2447", ""),
    ],
)
def test_result(part_name: Literal["a", "b"], expected: str, provided_input: str) -> None:
    if expected == "CHANGEME":
        pytest.skip()
    mod_path = get_mod_path(int(yearday[:4]), int(yearday[-2:]), part_name)
    mod = importlib.import_module(mod_path)
    assert mod.main(provided_input=provided_input) == expected
