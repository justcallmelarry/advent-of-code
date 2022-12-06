import importlib
import re
from typing import Literal

import pytest

yearday = re.sub("[^0-9]", "", str(__file__))


@pytest.mark.parametrize(
    ("part_name", "expected", "sample", "provided_input"),
    [
        ("a", "7", True, ""),
        ("a", "5", True, "bvwbjplbgvbhsrlpgdmjqwftvncz"),
        ("a", "6", True, "nppdvjthqldpwncqszvftbrmjlhg"),
        ("a", "10", True, "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"),
        ("a", "11", True, "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"),
        ("b", "19", True, ""),
        ("b", "19", True, "mjqjpqmgbljsphdztnvjfqwrcgsmlb"),
        ("b", "23", True, "bvwbjplbgvbhsrlpgdmjqwftvncz"),
        ("b", "23", True, "nppdvjthqldpwncqszvftbrmjlhg"),
        ("b", "29", True, "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"),
        ("b", "26", True, "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"),
        ("a", "1647", False, ""),
        ("b", "2447", False, ""),
    ],
)
def test_result(part_name: Literal["a", "b"], expected: str, sample: bool, provided_input: str) -> None:
    if expected == "CHANGEME":
        pytest.skip()
    mod = importlib.import_module(f"{yearday[:4]}.{str(yearday[-2:]).zfill(2)}.{part_name}")
    assert mod.main(sample=sample, provided_input=provided_input) == expected
