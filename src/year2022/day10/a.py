from injection import input_injection


@input_injection
def main(_input: str) -> str:
    result: int = 0

    cycles = 1
    register_x = 1
    for line in _input.splitlines():
        add_x = 0
        match line.split():
            case ["noop"]:
                current_cycles = 1
            case ["addx", number]:
                current_cycles = 2
                add_x = int(number)

        for _ in range(current_cycles):
            if cycles % 40 == 20:
                result += register_x * cycles
            cycles += 1
        register_x += add_x

    return str(result)


if __name__ == "__main__":
    print(main())
