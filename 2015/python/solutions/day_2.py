def mul(a: int, b: int) -> int:
    return 2 * a * b


def day_2(input: str) -> None:
    presents = input.strip().split("\n")
    wrap = 0
    ribbon = 0
    for present in presents:
        [l, w, h] = map(lambda x: int(x), present.split("x"))
        a, b, c = mul(l, w), mul(w, h), mul(h, l)
        slack = min(a, b, c) / 2
        wrap += int(slack) + a + b + c

        [m_1, m_2] = sorted([l, w, h])[:2]
        ribbon += 2 * m_1 + 2 * m_2 + l * w * h

    print("part_1", wrap)
    print("part_2", ribbon)
