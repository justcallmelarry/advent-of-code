import importlib
import os
import webbrowser
from datetime import date
from shutil import copyfile
from typing import Literal

import click


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option("-y", "--year", type=int, default=date.today().year)
@click.option("-d", "--day", type=int, default=date.today().day)
def new(year: int, day: int) -> None:
    day_path = os.path.join(str(year), f"{day}".zfill(2))

    if os.path.isdir(day_path):
        print("day alreddy exists")
    else:
        os.makedirs(day_path)
        dest_path_file_name = os.path.join(day_path, "a.py")
        if not os.path.exists(dest_path_file_name):
            copyfile("templates/base.py", dest_path_file_name)

        test_dest_path_file_name = os.path.join(
            os.path.dirname(__file__),
            "tests",
            str(year),
            f"test_{year}_{str(day).zfill(2)}.py",
        )
        if not os.path.exists(test_dest_path_file_name):
            copyfile("templates/test.py", test_dest_path_file_name)

    webbrowser.open(f"https://adventofcode.com/{year}/day/{day}")


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


if __name__ == "__main__":
    cli()
