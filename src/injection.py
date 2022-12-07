import inspect
import re
from typing import Callable

import aoc


def input_injection(func: Callable) -> Callable:
    def wrapper(provided_input: str = "") -> str:
        func_mod_path = inspect.getfile(func)
        yearday = re.sub("[^0-9]", "", str(func_mod_path))

        if provided_input:
            _input = provided_input
        else:
            _input = aoc.get_actual(day=int(yearday[-2:]), year=int(yearday[:4]))

        return func(_input)

    return wrapper
