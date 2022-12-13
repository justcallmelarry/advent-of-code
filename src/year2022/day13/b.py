import ast

from injection import input_injection
from year2022.day13.a import signal_order_check


@input_injection
def main(_input: str) -> str:
    """
    my original solution used bubble sort, but we only need to know how many signals the
    packet actually compares favourably against, letting us do less comparisons
    """
    result: int = 0

    signals = [ast.literal_eval(x) for x in _input.split()]

    # add one because index starts at 1
    position_1 = sum(1 for signal in signals if signal_order_check(signal, [[2]])) + 1
    # add two since first packet is also added already
    position_2 = sum(1 for signal in signals if signal_order_check(signal, [[6]])) + 2

    result = position_1 * position_2

    return str(result)


if __name__ == "__main__":
    print(main())
