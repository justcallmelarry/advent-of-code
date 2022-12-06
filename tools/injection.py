import inspect
from typing import Callable

import aoc


def input_injection(func: Callable) -> Callable:
    def wrapper(provided_input: str = "") -> str:
        func_mod_path = inspect.getfile(func)
        _, year, day = func_mod_path.rsplit("/", 3)[:3]

        if provided_input:
            _input = provided_input
        else:
            _input = aoc.get_actual(day=int(day), year=int(year))

        return func(_input)

    return wrapper
