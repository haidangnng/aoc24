def day_1(input: str) -> None:
    updated = False
    count = 0
    pos = 0
    for index, i in enumerate(input):
        count += 1 if i == "(" else -1
        if count == -1 and not updated:
            pos = index + 1
            updated = True
    print("part_1", count)
    print("part_2", pos)

