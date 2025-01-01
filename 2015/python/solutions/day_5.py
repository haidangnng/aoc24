import re

VOWELS = ["a", "i", "e", "u", "o"]
FORBIDDEN = ["ab", "cd", "pq", "xy"]


def is_three_vowels(input: str) -> bool:
    count = 0
    i = 0
    while i < len(input):
        count += 1 if input[i] in VOWELS else 0
        if count == 3:
            return True
        i += 1

    return False


def is_not_forbidden(input: str) -> bool:
    i = 0
    while i < len(input):
        dbl = input[i: i + 2]
        if dbl in FORBIDDEN:
            return False
        i += 1
    return True


def is_twice(input: str) -> bool:
    i = 0
    while i < len(input) - 1:
        if input[i] == input[i + 1]:
            return True
        i += 1
    return False


def is_nice(name: str) -> bool:
    return is_three_vowels(name) and is_not_forbidden(name) and is_twice(name)


def part_1(input: str) -> None:
    names = input.strip().split("\n")
    count = 0
    for i in names:
        count += 1 if is_nice(i) else 0
    print(f"part_1: {count}")


def is_contain_pair(string):
    return bool(re.search(r"([a-z][a-z]).*\1", string))


def is_contain_repeat_letter(string):
    return bool(re.search(r"([a-z])[a-z]\1", string))


def part_2(input: str) -> None:
    names = input.strip().split("\n")
    count = 0
    for i in names:
        count += 1 if is_contain_pair(i) and is_contain_repeat_letter(i) else 0
    print(f"part_2: {count}")


def day_5(input: str) -> None:
    part_1(input)
    part_2(input)
    return
