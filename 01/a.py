import os

import utils

if __name__ == "__main__":
    day = os.path.dirname(os.path.abspath(__file__)).rsplit("/", 1)[-1]
    _input = utils.get_actual(day=int(day), year=2022)

    elves = []

    current_elf = 0
    for i in _input.splitlines():
        if i:
            current_elf += int(i)
        else:
            elves.append(current_elf)
            current_elf = 0

    print(max(elves))
