from collections import defaultdict
from pprint import pprint

from utils import read_lines


def main():
    # lines = read_lines("day_9/test.txt")
    lines = read_lines("day_9/input.txt")
    line = lines[0]
    disk = []
    cid = 0
    for i, v in enumerate(line):
        if i % 2 == 0:
            disk = disk + [cid for _ in range(0, int(v))]
            cid += 1
        else:
            disk = disk + ["." for _ in range(0, int(v))]
    l, r = 0, len(disk) - 1
    while l < r:
        if disk[r] == ".":
            r -= 1
            continue
        if disk[l] == "." and disk[r] != ".":
            disk[l], disk[r] = disk[r], disk[l]
            r -= 1
        l += 1
    res = 0
    for i, v in enumerate(disk):
        if v == ".":
            break
        res += v * i
    print(res)


def part_two():
    # lines = read_lines("day_9/test.txt")
    lines = read_lines("day_9/input.txt")
    line = lines[0]
    disk = []
    cid = 0
    for i, v in enumerate(line):
        if i % 2 == 0:
            disk = disk + [cid for _ in range(0, int(v))]
            cid += 1
        else:
            disk = disk + ["." for _ in range(0, int(v))]

    l, m, r = 0, 0, len(disk) - 1
    while l < r:
        if disk[r] == ".":
            r -= 1
            continue
        if disk[l] == "." and disk[r] != ".":
            disk[l], disk[r] = disk[r], disk[l]
            r -= 1
        l += 1
    res = 0
    for i, v in enumerate(disk):
        if v == ".":
            break
        res += v * i
    print(res)


part_two()
