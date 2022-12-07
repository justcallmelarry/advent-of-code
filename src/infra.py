import os
from functools import lru_cache
from typing import Literal


@lru_cache(1)
def get_day_path(year: int, day: int) -> str:
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(root_dir, "src", f"year{year}", "day" + str(day).zfill(2))


def get_mod_path(year: int, day: int, part_name: Literal["a", "b"]) -> str:
    return f"year{year}.day{str(day).zfill(2)}.{part_name}"
