import math
from collections import defaultdict
from functools import reduce

from utils import read_lines


def update_rules(rules, a, b):
    if rules.get(a):
        rules[a].append(b)
    else:
        rules[a] = [b]
    return rules


def check_query(rules, target, value):
    return value in rules[target]


def get_middle(arr):
    mid = math.floor(len(arr) / 2)
    return arr[mid]


def part_one():
    lines = read_lines("day_5/input.txt")

    is_query = False
    bf_rules = defaultdict(list)
    af_rules = defaultdict(list)

    cr_list = []
    id = 0

    for line in lines:
        if line == "":
            is_query = True
            continue
        if not is_query:
            [before, after] = line.split("|")
            before, after = int(before), int(after)
            update_rules(bf_rules, after, before)
            update_rules(af_rules, before, after)
        else:
            is_correct = True
            sequence = [int(p) for p in line.split(",")]
            for i, page in enumerate(sequence):
                for j, el in enumerate(sequence):
                    if not is_correct:
                        break
                    if i == j:
                        continue
                    if j < i:
                        is_correct = check_query(bf_rules, page, el)
                    else:
                        is_correct = check_query(af_rules, page, el)
                if not is_correct:
                    break

            if is_correct:
                cr_list.append(sequence)
            id += 1

    sum = reduce(
        lambda a, b: (
            get_middle(a) + get_middle(b) if isinstance(a, list) else a + get_middle(b)
        ),
        cr_list,
    )
    print(sum)


def part_two():
    lines = read_lines("day_5/input.txt")

    is_query = False
    bf_rules = defaultdict(list)
    af_rules = defaultdict(list)

    cr_list = []
    id = 0

    for line in lines:
        if line == "":
            is_query = True
            continue
        if not is_query:
            [before, after] = line.split("|")
            before, after = int(before), int(after)
            update_rules(bf_rules, after, before)
            update_rules(af_rules, before, after)
        else:
            is_correct = True
            sequence = [int(p) for p in line.split(",")]
            for i, page in enumerate(sequence):
                for j, el in enumerate(sequence):
                    if i == j:
                        continue
                    if j < i:
                        is_correct = check_query(bf_rules, page, el)
                    else:
                        is_correct = check_query(af_rules, page, el)
                    if not is_correct:
                        break
                if not is_correct:
                    break

            if not is_correct:
                cr_list.append(sequence)
            id += 1

    l = 0
    for line in cr_list:
        print(f"line: {line}")
        for i, a in enumerate(line):
            before, after = 0, 0
            for j, b in enumerate(line):
                if i == j:
                    continue
                if check_query(bf_rules, a, b):
                    before += 1
                elif check_query(af_rules, a, b):
                    after += 1
            if before == after:
                l += a
    print(l)


part_two()
