import os
from typing import Callable

import utils


def input_injection(func: Callable) -> Callable:
    def wrapper(sample: bool):
        func_mod_path = func.__module__
        year, day = func_mod_path.rsplit(".")[:2]
        if sample:
            _input = utils.get_sample(day=day, year=int(year))

        _input = utils.get_actual(day=int(day), year=int(year))
        return func(_input, sample)

    return wrapper
