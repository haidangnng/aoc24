import re

lights = [0 for _ in range(1_000_000)]


def parse_command(cmd: str):
    pattern = r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)"
    match = re.match(pattern, cmd)
    if match:
        return (
            match.group(1),
            int(match.group(2)),
            int(match.group(3)),
            int(match.group(4)),
            int(match.group(5)),
        )


def part_1(input) -> None:
    ins = input.strip().split("\n")
    for cmd in ins:
        (action, x1, x2, y1, y2) = parse_command(cmd)
        for i in range(x1, y1 + 1):
            for j in range(x2, y2 + 1):
                index = 1000 * i + j
                if action == "turn off":
                    lights[index] = 0
                if action == "turn on":
                    lights[index] = 1
                if action == "toggle":
                    lights[index] = 1 if lights[index] == 0 else 0

    count = 0
    for i in lights:
        count += i
    print(f"part_1: {count}")


def part_2(input) -> None:
    ins = input.strip().split("\n")
    for cmd in ins:
        (action, x1, x2, y1, y2) = parse_command(cmd)
        for i in range(x1, y1 + 1):
            for j in range(x2, y2 + 1):
                index = 1000 * i + j
                if action == "turn off":
                    lights[index] -= 1 if lights[index] > 0 else 0
                if action == "turn on":
                    lights[index] += 1
                if action == "toggle":
                    lights[index] += 2

    count = 0
    for i in lights:
        count += i

    print(f"part_2: {count}")


def day_6(input: str) -> None:
    part_2(input)
