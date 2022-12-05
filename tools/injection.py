import inspect
from typing import Callable

import aoc


def input_injection(func: Callable) -> Callable:
    def wrapper(sample: bool) -> str:
        func_mod_path = inspect.getfile(func)
        _, year, day = func_mod_path.rsplit("/", 3)[:3]

        if sample:
            _input = aoc.get_sample(day=day, year=int(year))
        else:
            _input = aoc.get_actual(day=int(day), year=int(year))

        return func(_input, sample)

    return wrapper
