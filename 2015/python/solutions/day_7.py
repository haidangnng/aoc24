import re

book = {}


def parse_line(line: str):
    pattern = r"(.+?)\s*->\s*(.+)"
    match = re.match(pattern, line)

    if match:
        return (match.group(1), match.group(2))


def get_bitwise(cmd, x, y=None):
    res = 0
    if cmd == "AND":
        res = (x & y) & 0xFFFF
        pass
    if cmd == "OR":
        res = (x | y) & 0xFFFF
        pass
    if cmd == "RSHIFT":
        res = x.rotateRight(y)
        pass
    if cmd == "LSHIFT":
        res = x.rotateLeft(y)
        pass
    if cmd == "NOT":
        res = ~x & 0xFFFF

    return res


def get_value(input):
    print(book[input])
    val = book[input]
    try:
        return int(val)
    except ValueError:
        return


def day_7(input: str) -> None:
    circuit = input.strip().split("\n")

    for line in circuit:
        (assignment, target) = parse_line(line)
        book[target] = assignment

    value = get_value("a")
