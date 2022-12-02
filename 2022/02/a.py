import sys
from collections import Counter

from injection import input_injection


def score(opp: int, me: int) -> int:
    """
    If a value A is one lower than value B, A wins
    Use modulo to end up with positive values
    Always return +1 since modulo A is 0, but should give 1 point
    """
    if (opp - 1) % 3 == me:
        return me + 1  # loss, return value of own value

    elif (me - 1) % 3 == opp:
        return me + 7  # win, return value of own value + 6

    # draw, return value of own value + 3
    return me + 4


@input_injection
def main(_input: str, sample_input: bool = False) -> str:
    result: int = 0

    ord_a = ord("A")
    ord_x = ord("X")

    # since there are only 9 possible inputs, group them to do fewer calculations
    grouped = Counter(_input.splitlines())
    for game in grouped:
        opp, me = game.split()

        result += score(ord(opp) - ord_a, ord(me) - ord_x) * grouped[game]

    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
