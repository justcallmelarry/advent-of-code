import os

from infra import get_day_path, get_mod_path

_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_get_day_path() -> None:
    assert get_day_path(2022, 7) == os.path.join(_root_dir, "src", "year2022", "day07")

def test_get_mod_path() -> None:
    assert get_mod_path(2022, 7, "a") == "year2022.day07.a"
