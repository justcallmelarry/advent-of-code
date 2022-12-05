import importlib
import os
import webbrowser
from datetime import date
from functools import lru_cache
from shutil import copyfile
from typing import Literal

import aoc
import click


@lru_cache(1)
def _get_day_path(year: int, day: int) -> str:
    return os.path.join(str(year), f"{day}".zfill(2))


def _store_markdown(year: int, day: int) -> None:
    day_path = _get_day_path(year, day)
    markdown = aoc.get_markdown(year=year, day=day)
    with open(os.path.join(day_path, "README.md"), "w") as readme:
        readme.write(markdown)


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option("-y", "--year", type=int, default=date.today().year)
@click.option("-d", "--day", type=int, default=date.today().day)
def new(year: int, day: int) -> None:
    day_path = _get_day_path(year, day)

    if os.path.isdir(day_path):
        print("day alreddy exists")
    else:
        os.makedirs(day_path)
        dest_path_file_name = os.path.join(day_path, "a.py")
        if not os.path.exists(dest_path_file_name):
            copyfile("templates/base.py", dest_path_file_name)

        test_year_dir_path = os.path.join(
            os.path.dirname(__file__),
            "tests",
            str(year),
        )
        if not os.path.isdir(test_year_dir_path):
            os.makedirs(test_year_dir_path)
        test_dest_path_file_name = os.path.join(
            test_year_dir_path,
            f"test_{year}_{str(day).zfill(2)}.py",
        )
        if not os.path.exists(test_dest_path_file_name):
            copyfile("templates/test.py", test_dest_path_file_name)

    webbrowser.open(aoc.get_url(year, day))
    _store_markdown(year, day)


@cli.command()
@click.argument("part", type=click.Choice(["1", "2"]))
@click.option("-y", "--year", type=int, default=date.today().year)
@click.option("-d", "--day", type=int, default=date.today().day)
@click.option("-s", "--sample", is_flag=True)
def run(part: Literal["1", "2"], year: int, day: int, sample: bool) -> None:
    part_name = "a" if part == "1" else "b"
    mod = importlib.import_module(f"{year}.{str(day).zfill(2)}.{part_name}")

    result = mod.main(sample)

    print(f"Part {part}:", result)


@cli.command()
@click.option("-y", "--year", type=int, default=date.today().year)
@click.option("-d", "--day", type=int, default=date.today().day)
def markdown(year: int, day: int) -> None:
    _store_markdown(year, day)


if __name__ == "__main__":
    cli()
