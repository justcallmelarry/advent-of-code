import math

from injection import input_injection
from year2022.day21.a import get_monkeys, monkey_math


@input_injection
def main(_input: str) -> str:
    monkeys = get_monkeys(_input)

    # replace the root value so that we get minus, which we will use to check for 0
    root_value = monkeys["root"]
    monkey_a, _, monkey_b = str(root_value).split()
    monkeys["root"] = f"{monkey_a} - {monkey_b}"

    # get original value for comparison
    baseline = monkey_math(monkeys, "root")
    og_sign = math.copysign(1, baseline)

    span = (0, int("9" * (len(str(baseline)) + 1)))
    while baseline != 0:
        half = sum(span) // 2
        monkeys["humn"] = half
        baseline = monkey_math(monkeys, "root")

        if math.copysign(1, baseline) == og_sign:
            span = (half + 1, span[1])
        else:
            span = (span[0], half - 1)

    return str(half)


if __name__ == "__main__":
    print(main())
