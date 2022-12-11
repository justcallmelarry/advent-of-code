import heapq
import math

from injection import input_injection
from year2022.day11.a import get_monkeys


@input_injection
def main(_input: str) -> str:
    result: int = 0

    monkeys = get_monkeys(_input)
    lcm = math.lcm(*[x.test for x in monkeys])

    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                # inspection
                item = monkey.inspect(item)

                # reduce worry
                item %= lcm

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
