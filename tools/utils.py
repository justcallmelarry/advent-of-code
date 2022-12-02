# mostly stolen from mcpower
import os
import re
import sys
from typing import Any, Callable

sys.setrecursionlimit(10**6)


def lmap(func: Callable, *iterables: Any) -> list:
    return list(map(func, *iterables))


def make_grid(*dimensions: list[int], fill: Any = None) -> list:
    "Returns a grid such that 'dimensions' is juuust out of bounds."
    if len(dimensions) == 1:
        return [fill for _ in range(dimensions[0])]  # type: ignore
    next_down = make_grid(*dimensions[1:], fill=fill)
    return [list(next_down) for _ in range(dimensions[0])]  # type: ignore


def min_max(list_: list) -> tuple:
    return min(list_), max(list_)


def max_minus_min(list_: list) -> int:
    return max(list_) - min(list_)


def flatten(list_: list) -> list:
    return [i for x in list_ for i in x]


def ints(s: str) -> list[int]:
    return lmap(int, re.findall(r"-?\d+", s))


def positive_ints(s: str) -> list[int]:
    return lmap(int, re.findall(r"\d+", s))


def floats(s: str) -> list[float]:
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))


def positive_floats(s: str) -> list[float]:
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))


def words(s: str) -> list[str]:
    return re.findall(r"[a-zA-Z]+", s)


def get_sample(day: int, year: int) -> str:
    input_destination_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        str(year),
        f"{day}".zfill(2),
        "input.sample",
    )
    try:
        with open(input_destination_path) as sample_input:
            return sample_input.read()
    except FileNotFoundError:
        print("no sample file saved")
        sys.exit(1)


def get_token() -> str:
    from pathlib import Path

    token_path = Path(__file__).parent.parent / "token.txt"
    with open(token_path) as f:
        return f.read().strip()


def get_actual(day: int, year: int) -> str:
    input_destination_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        str(year),
        f"{day}".zfill(2),
        "input.user",
    )
    try:
        with open(input_destination_path) as actual_input:
            return actual_input.read()
    except FileNotFoundError:
        pass

    # is it time?
    from datetime import datetime, timedelta, timezone

    est = timezone(timedelta(hours=-5))
    unlock_time = datetime(year, 12, day, tzinfo=est)
    cur_time = datetime.now(tz=est)
    delta = unlock_time - cur_time
    if delta.days >= 0:
        print(f"Remaining time until unlock: {delta}")
        return ""

    import httpx

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    response = httpx.get(url, cookies={"session": get_token()})
    response.raise_for_status()
    with open(input_destination_path, "w") as input_file:
        input_file.write(response.text)

    print("Input saved!")
    return response.text


def manhattan_dist(coords: tuple[int, int], target_coords: tuple[int, int]) -> int:
    dx = abs(coords[0] - target_coords[0])
    dy = abs(coords[1] - target_coords[1])
    return abs(dx + dy)
