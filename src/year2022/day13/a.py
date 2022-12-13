import ast
import itertools

from injection import input_injection


class ContinueParsing(Exception):
    pass


def signal_order_check(left: list | int, right: list | int) -> bool:
    a = [left] if isinstance(left, int) else left
    b = [right] if isinstance(right, int) else right

    for av, bv in itertools.zip_longest(a, b):
        if av is None:
            return True
        elif bv is None:
            return False

        elif any(isinstance(x, list) for x in (av, bv)):
            try:
                return signal_order_check(av, bv)
            except ContinueParsing:
                pass
        else:
            if bv > av:
                return True
            if av > bv:
                return False

    raise ContinueParsing


@input_injection
def main(_input: str) -> str:
    result: int = 0

    pairs = _input.split("\n\n")

    for i, pair in enumerate(pairs, start=1):
        lines = pair.splitlines()

        left = ast.literal_eval(lines[0])
        right = ast.literal_eval(lines[1])

        correct = signal_order_check(left, right)
        if correct:
            result += i

    return str(result)


if __name__ == "__main__":
    print(main())
