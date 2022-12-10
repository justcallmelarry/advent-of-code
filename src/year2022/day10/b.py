from injection import input_injection


@input_injection
def main(_input: str) -> str:
    filled_char = "#"
    empty_char = "."

    output = ""

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
            in_sprite = (register_x - 1) <= (cycles - 1) % 40 <= (register_x + 1)
            output += filled_char if in_sprite else empty_char

            if cycles % 40 == 0:
                output += "\n"

            cycles += 1

        register_x += add_x

    return "\n" + output


if __name__ == "__main__":
    print(main())
