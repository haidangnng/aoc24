from collections import defaultdict
from pprint import pprint

from utils import read_lines


def main():
    lines = read_lines("day_8/test.txt")
    # lines = read_lines("day_8/input.txt")
    map = defaultdict(set)
    for r, line in enumerate(lines):
        for c, i in enumerate(line):
            if i == ".":
                continue
            else:
                pos = (r, c)
                if map.get(i):
                    map[i].add(pos)
                else:
                    map[i] = {pos}

    res = set()
    for i in [*map.keys()]:
        li = list(map.get(i))
        for cur in range(0, len(li)):
            for next in range(cur + 1, len(li)):
                # print(f"cur: {li[cur]}, next:{li[next]}")
                (a, b) = li[cur]
                (c, d) = li[next]
                x_1 = 2 * c - a
                y_1 = 2 * d - b
                if (
                    0 <= x_1
                    and x_1 <= len(lines) - 1
                    and 0 <= y_1
                    and y_1 <= len(lines[0]) - 1
                ):
                    res.add((x_1, y_1))
                x_2 = 2 * a - c
                y_2 = 2 * b - d
                if (
                    0 <= x_2
                    and x_2 <= len(lines) - 1
                    and 0 <= y_2
                    and y_2 <= len(lines[0]) - 1
                ):
                    res.add((x_2, y_2))

    print(len(res))


def two():
    lines = read_lines("day_8/test.txt")
    # lines = read_lines("day_8/input.txt")
    map = defaultdict(set)
    for r, line in enumerate(lines):
        for c, i in enumerate(line):
            if i == ".":
                continue
            else:
                pos = (r, c)
                if map.get(i):
                    map[i].add(pos)
                else:
                    map[i] = {pos}

    lines = [list(row) for row in lines]
    res = set()
    for i in [*map.keys()]:
        li = list(map.get(i))
        for cur in range(0, len(li)):
            for next in range(cur + 1, len(li)):
                # print(f"cur: {li[cur]}, next:{li[next]}")
                (a, b) = li[cur]
                (c, d) = li[next]
                x_1 = 2 * c - a
                y_1 = 2 * d - b
                if (
                    0 <= x_1
                    and x_1 <= len(lines) - 1
                    and 0 <= y_1
                    and y_1 <= len(lines[0]) - 1
                ):
                    res.add((x_1, y_1))
                    if lines[x_1][y_1] == ".":
                        lines[x_1][y_1] = "#"

                x_2 = 2 * a - c
                y_2 = 2 * b - d
                if (
                    0 <= x_2
                    and x_2 <= len(lines) - 1
                    and 0 <= y_2
                    and y_2 <= len(lines[0]) - 1
                ):
                    res.add((x_2, y_2))
                    if lines[x_2][y_2] == ".":
                        lines[x_2][y_2] = "#"

    pprint(["".join(line) for line in lines])
    print(res)


two()
