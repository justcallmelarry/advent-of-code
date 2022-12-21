import operator

from injection import input_injection

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}


def get_monkeys(_input: str) -> dict[str, str | int]:
    monkeys: dict[str, str | int] = {}

    for line in _input.splitlines():
        name, value = line.split(": ")
        if value.isnumeric():
            monkeys[name] = int(value)
        else:
            monkeys[name] = value

    return monkeys


def monkey_math(monkeys: dict[str, str | int], target: str) -> int:
    target_value = monkeys[target]
    if isinstance(target_value, int):
        return target_value

    monkey_a, operation, monkey_b = target_value.split()
    return operators[operation](monkey_math(monkeys, monkey_a), monkey_math(monkeys, monkey_b))


@input_injection
def main(_input: str) -> str:
    monkeys = get_monkeys(_input)
    result = monkey_math(monkeys, "root")

    return str(result)


if __name__ == "__main__":
    print(main())
