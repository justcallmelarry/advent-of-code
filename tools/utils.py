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


def get_sample(day: int) -> str:
    input_destination_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        f"{day}".zfill(2),
        "input.sample",
    )
    try:
        with open(input_destination_path) as sample_input:
            return sample_input.read()
    except FileNotFoundError:
        print("no sample file saved")
        sys.exit(1)


def get_actual(day: int | None = None, year: int | None = None) -> str:
    input_destination_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        f"{day}".zfill(2),
        "input.user",
    )
    try:
        with open(input_destination_path) as actual_input:
            return actual_input.read()
    except FileNotFoundError:
        pass
    from pathlib import Path

    # let's try grabbing it
    search_path = Path(".").resolve()
    try:
        if day is None:
            day = int(search_path.name)
        if year is None:
            year = int(search_path.parent.name)
    except ValueError:
        print("Can't get day and year.")
        print("Backup: save 'input.user' into the same folder as this script.")
        return ""

    print(f"{year} day {day} input not found.")

    # is it time?
    from datetime import datetime, timedelta, timezone

    est = timezone(timedelta(hours=-5))
    unlock_time = datetime(year, 12, day, tzinfo=est)
    cur_time = datetime.now(tz=est)
    delta = unlock_time - cur_time
    if delta.days >= 0:
        print(f"Remaining time until unlock: {delta}")
        return ""

    while (not list(search_path.glob("*/token.txt"))) and search_path.parent != search_path:
        search_path = search_path.parent

    token_files = list(search_path.glob("*/token.txt"))
    if not token_files:
        assert search_path.parent == search_path
        print("Can't find token.txt in a parent directory.")
        print("Backup: save 'input.user' into the same folder as this script.")
        return ""

    with token_files[0].open() as f:
        token = f.read().strip()

    # importing requests takes a long time...
    # let's do it without requests.
    import shutil
    import urllib.error
    import urllib.request

    opener = urllib.request.build_opener()
    opener.addheaders = [
        ("Cookie", f"session={token}"),
        ("User-Agent", "python-requests/2.19.1"),
    ]
    print("Sending request...")
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    try:
        with opener.open(url) as r:
            with open(input_destination_path, "wb") as f:
                shutil.copyfileobj(r, f)
            print("Input saved!")
            return open(input_destination_path).read()
    except urllib.error.HTTPError as e:
        status_code = e.getcode()
        if status_code == 400:
            print("Auth failed!")
        elif status_code == 404:
            print("Day is not out yet????")
        else:
            print(f"Request failed with code {status_code}??")
        return ""


def manhattan_dist(coords: tuple[int, int], target_coords: tuple[int, int]) -> int:
    dx = abs(coords[0] - target_coords[0])
    dy = abs(coords[1] - target_coords[1])
    return abs(dx + dy)
