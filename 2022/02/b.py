import sys

import injection


def score(opp: int, me: int) -> int:
    # if opp == 1 value lower than me -> loss
    if (opp - 1) % 3 == me:
        return me + 1

    # if me == 1 value lower than opp -> win
    elif (me - 1) % 3 == opp:
        return me + 7

    # draw
    return me + 4


@injection.input_injection
def main(_input: str, sample_input: bool = False) -> str:
    result: str | int = 0

    ord_a = ord("A")
    ord_x = ord("X")

    total_score = 0
    for game in _input.splitlines():
        opp, instruction = game.split()

        # add opp value together with the instruction value and figure out the move before it
        me = (ord(opp) - ord_a + ord(instruction) - ord_x - 1) % 3

        total_score += score(ord(opp) - ord_a, me)

    result = total_score
    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
