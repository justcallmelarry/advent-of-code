import ast
import functools

from injection import input_injection
from year2022.day13.a import signal_order_check


def compare_sorter(a: list | int, b: list | int) -> int:
    if signal_order_check(a, b):
        return -1
    return 1


@input_injection
def part_2(_input: str) -> str:
    result: int = 0

    packet_a = [[2]]
    packet_b = [[6]]

    signals = [ast.literal_eval(x) for x in _input.split()] + [packet_a, packet_b]

    signals.sort(key=functools.cmp_to_key(compare_sorter))
    result = (signals.index(packet_a) + 1) * (signals.index(packet_b) + 1)

    return str(result)


if __name__ == "__main__":
    print(part_2())
