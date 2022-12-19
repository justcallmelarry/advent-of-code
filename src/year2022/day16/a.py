from __future__ import annotations

from collections import deque
from dataclasses import dataclass

from injection import input_injection


@dataclass
class Valve:
    name: str
    flow_rate: int
    tunnels: list[Valve]

    def go_to(self, name: str) -> Valve:
        for v in self.tunnels:
            if v.name == name:
                return v

        raise Exception("No such tunnel")

    def __repr__(self) -> str:
        return f"Valve({self.name} flow_rate={self.flow_rate}"


@dataclass
class Volcano:
    current_position: Valve
    valves: dict[str, Valve]
    opened: list[str]
    total: int = 0
    current_flow: int = 0
    minutes_lapsed: int = 1

    @property
    def sorted_opened(self) -> tuple[str, ...]:
        return tuple(sorted(self.opened))

    @property
    def end_total(self, end: int = 26) -> int:
        return self.total + self.current_flow * (end - self.minutes_lapsed - 1)


def get_valves(_input: str) -> dict[str, Valve]:
    valves: dict[str, Valve] = {}

    for line in _input.splitlines():
        x = line.split()
        name = x[1]
        flow_rate = int(x[4].split("=")[-1].strip(";"))

        if not name in valves:
            valves[name] = Valve(name=name, flow_rate=0, tunnels=[])

        valve = valves[name]
        valve.flow_rate = flow_rate

        for tunnel_name in x[9:]:
            tunnel_name = tunnel_name.strip(",")
            if tunnel_name not in valves:
                valves[tunnel_name] = Valve(name=tunnel_name, flow_rate=0, tunnels=[])
            tunnel_valve = valves[tunnel_name]
            valve.tunnels.append(tunnel_valve)

    return valves


@dataclass
class QeueuItem:
    valve: Valve
    path: deque[str]


__CACHE: dict[tuple[str, str], int] = {}


def get_shortest_path(start: Valve, target: Valve) -> int:
    if (start.name, target.name) in __CACHE:
        return __CACHE[(start.name, target.name)]
    q = deque([QeueuItem(valve=start, path=deque([]))])
    seen: set[str] = set([])

    while q:
        cur = q.popleft()
        for t in cur.valve.tunnels:
            if t.name in seen:
                continue

            new_path = cur.path.copy()
            new_path.append(t.name)

            if t == target:
                __CACHE[(start.name, target.name)] = len(new_path)
                return len(new_path)

            seen.add(t.name)
            q.append(QeueuItem(valve=t, path=new_path))

    raise Exception("Not found")


class NextVolcano(Exception):
    pass


def volcano_game(original_state: Volcano) -> int:
    volcanoes: deque[Volcano] = deque([original_state])
    biggest = 0

    possible_turnons = [t for t in original_state.valves.values() if t.flow_rate != 0]

    while volcanoes:
        volcano = volcanoes.pop()
        current_position = volcano.current_position
        try:
            for minute in range(volcano.minutes_lapsed, 31):
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
                    if minute + shortest <= 30:
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
        if volcano.total > biggest:
            biggest = volcano.total

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
