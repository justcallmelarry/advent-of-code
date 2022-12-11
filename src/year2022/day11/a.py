import heapq
from dataclasses import dataclass

import utils
from injection import input_injection


@dataclass
class Monkey:
    number: int
    items: list[int]
    operation: list[str]
    test: int
    if_true: int
    if_false: int

    inspections: int = 0

    def inspect(self, item: int) -> int:
        operation_value = self.operation[4]
        if operation_value.isnumeric():
            number = int(operation_value)
        elif operation_value == "old":
            number = item

        if self.operation[3] == "*":
            item *= number
        elif self.operation[3] == "+":
            item += number

        self.inspections += 1

        return item


def get_monkeys(_input: str) -> list[Monkey]:
    monkey_inputs = _input.split("\n\n")
    monkeys: list[Monkey] = []

    for monkey_input in monkey_inputs:
        monkey_lines = monkey_input.splitlines()
        monkeys.append(
            Monkey(
                number=utils.intify(monkey_lines[0]),
                items=utils.ints(monkey_lines[1]),
                operation=monkey_lines[2].strip().replace("Operation: ", "").split(),
                test=utils.intify(monkey_lines[3]),
                if_true=utils.intify(monkey_lines[4]),
                if_false=utils.intify(monkey_lines[5]),
            )
        )

    return monkeys


@input_injection
def main(_input: str) -> str:
    result: int = 0

    monkeys = get_monkeys(_input)

    for _ in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                item = monkey.inspect(item)

                # reduce worry
                item = item // 3

                # throw
                if item % monkey.test == 0:
                    monkeys[monkey.if_true].items.append(item)
                else:
                    monkeys[monkey.if_false].items.append(item)

            monkey.items = []

    a, b = heapq.nlargest(2, [monkey.inspections for monkey in monkeys])

    result = a * b
    return str(result)


if __name__ == "__main__":
    print(main())
