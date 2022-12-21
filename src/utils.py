# mostly stolen from mcpower
import re
import sys
from typing import Any, Callable

sys.setrecursionlimit(10**6)

FILLED_CHAR = "▓"


def lmap(func: Callable, *iterables: Any) -> list:
    return list(map(func, *iterables))


def min_max(list_: list) -> tuple[int, int]:
    return min(list_), max(list_)


def max_minus_min(list_: list) -> int:
    return max(list_) - min(list_)


def flatten(list_: list) -> list:
    return [i for x in list_ for i in x]


def ints(s: str) -> list[int]:
    return lmap(int, re.findall(r"-?\d+", s))


def intify(s: str) -> int:
    return int(re.sub("[^0-9]", "", s))


def positive_ints(s: str) -> list[int]:
    return lmap(int, re.findall(r"\d+", s))


def floats(s: str) -> list[float]:
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))


def positive_floats(s: str) -> list[float]:
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))


def words(s: str) -> list[str]:
    return re.findall(r"[a-zA-Z]+", s)


def manhattan_dist(coords: tuple[int, int], target_coords: tuple[int, int]) -> int:
    dx = abs(coords[0] - target_coords[0])
    dy = abs(coords[1] - target_coords[1])
    return abs(dx + dy)


def split_string(string: str, parts: int = 2) -> tuple[str, ...]:
    return string[: len(string) // parts], string[len(string) // parts :]


def overlaps(a: list[int], b: list[int]) -> range:
    return range(max(a[0], b[0]), min(a[-1], b[-1]) + 1)
