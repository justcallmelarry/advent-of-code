from collections import deque
from functools import lru_cache

from injection import input_injection
from year2022.day16.a import NextVolcano, Volcano, get_shortest_path, get_valves


@lru_cache(maxsize=None)
def intersects(a: tuple[str, ...], b: tuple[str, ...]) -> bool:
    if set(a).intersection(set(b)):
        return True
    return False


def volcano_game(original_state: Volcano) -> int:
    optimized_states: dict[tuple[str, ...], Volcano] = {}
    volcanoes: deque[Volcano] = deque([original_state])
    biggest = 0

    possible_turnons = [t for t in original_state.valves.values() if t.flow_rate != 0]

    while volcanoes:
        volcano = volcanoes.pop()
        current_position = volcano.current_position
        try:
            for minute in range(volcano.minutes_lapsed, 27):
                volcano.total += volcano.current_flow
                # open a valve
                if current_position.flow_rate != 0 and current_position.name not in volcano.opened:
                    volcano.current_flow += current_position.flow_rate
                    volcano.opened.append(current_position.name)
                    # volcano.minutes_lapsed = minute
                    continue

                # otherwise explore options
                for v in possible_turnons:
                    if v.name in volcano.opened or v == current_position:
                        continue

                    shortest = get_shortest_path(current_position, v)
                    if minute + shortest <= 26:
                        volcanoes.append(
                            Volcano(
                                current_position=v,
                                valves=volcano.valves,
                                opened=volcano.opened.copy(),
                                total=volcano.total + (shortest - 1) * volcano.current_flow,
                                current_flow=volcano.current_flow,
                                minutes_lapsed=minute + shortest,
                            )
                        )
                if len(volcano.opened) != len(possible_turnons):
                    raise NextVolcano
                volcano.minutes_lapsed = minute
        except NextVolcano:
            pass

        check = volcano.sorted_opened
        if check not in optimized_states:
            optimized_states[check] = volcano
        elif volcano.end_total > optimized_states[check].end_total:
            optimized_states[check] = volcano

    for me in optimized_states.values():
        for elephant in optimized_states.values():
            if me == elephant:
                # dont check yourself
                continue
            opened = sorted([me.sorted_opened, elephant.sorted_opened])
            if intersects(opened[0], opened[1]):
                # intersection exists, skip
                continue

            value = elephant.end_total + me.end_total

            if value > biggest:
                biggest = value

    return biggest


@input_injection
def main(_input: str) -> str:
    valves = get_valves(_input)
    result = 0

    aa = valves["AA"]
    volcano = Volcano(current_position=aa, valves=valves, opened=[])

    result = volcano_game(volcano)

    return str(result)


if __name__ == "__main__":
    print(main())
