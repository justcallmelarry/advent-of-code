import sys

import injection


def game_points(own: str, opp: str) -> int:
    if opp == own:
        return 3

    if own == "r" and opp == "s":
        return 6
    if own == "s" and opp == "p":
        return 6
    if own == "p" and opp == "r":
        return 6

    return 0


def get_points(a: str) -> int:
    if a == "r":
        return 1
    elif a == "p":
        return 2
    elif a == "s":
        return 3
    raise Exception


@injection.input_injection
def main(_input: str, sample_input: bool = False) -> str:
    result: str | int = 0

    hand_map = {
        "A": "r",
        "B": "p",
        "C": "s",
        "X": "r",
        "Y": "p",
        "Z": "s",
    }

    total_score = 0
    for game in _input.splitlines():
        opp, own = game.split()

        total_score += game_points(hand_map[own], hand_map[opp]) + get_points(hand_map[own])

    result = total_score
    return str(result)


if __name__ == "__main__":
    print(main(True if "--sample" in sys.argv else False))
