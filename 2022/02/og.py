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
def part_1(_input: str) -> str:
    result: int = 0

    r = 1
    p = 2
    s = 3
    draw = 3
    win = 6

    results = {
        "A X": r + draw,
        "A Y": p + win,
        "A Z": s,
        "B X": r,
        "B Y": p + draw,
        "B Z": s + win,
        "C X": r + win,
        "C Y": p,
        "C Z": s + draw,
    }

    for line in _input.splitlines():
        result += results[line]

    return str(result)


@input_injection
def part_2(_input: str) -> str:
    result: int = 0

    r = 1
    p = 2
    s = 3
    draw = 3
    win = 6

    results = {
        "A X": s,
        "B X": r,
        "C X": p,
        "A Y": r + draw,
        "B Y": p + draw,
        "C Y": s + draw,
        "A Z": p + win,
        "B Z": s + win,
        "C Z": r + win,
    }

    for line in _input.splitlines():
        result += results[line]

    return str(result)


if __name__ == "__main__":
    print(part_1(True if "--sample" in sys.argv else False))
    print(part_2(True if "--sample" in sys.argv else False))
