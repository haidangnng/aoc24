from utils import read_lines


def part_one():
    lines = read_lines("day_4/input.txt")
    count = 0
    lines = (
        ["." * (len(lines[0]) + 8)] * 3
        + ["...." + line + "...." for line in lines]
        + ["." * (len(lines[0]) + 8)] * 3
    )
    for row_index, row in enumerate(lines):
        for col, ele in enumerate(row):
            if ele != "X":
                continue

            else:
                # forward:
                if row[col : col + 4] == "MAS":
                    count += 1
                # backward:
                if row[col - 3 : col + 1] == "SAMX":
                    count += 1
                # up:
                if (
                    lines[row_index][col]
                    + lines[row_index - 1][col]
                    + lines[row_index - 2][col]
                    + lines[row_index - 3][col]
                    == "MAS"
                ):
                    count += 1

                if (
                    lines[row_index][col]
                    + lines[row_index - 1][col + 1]
                    + lines[row_index - 2][col + 2]
                    + lines[row_index - 3][col + 3]
                    == "MAS"
                ):
                    count += 1

                if (
                    lines[row_index][col]
                    + lines[row_index - 1][col - 1]
                    + lines[row_index - 2][col - 2]
                    + lines[row_index - 3][col - 3]
                    == "MAS"
                ):
                    count += 1

                if (
                    lines[row_index][col]
                    + lines[row_index + 1][col + 1]
                    + lines[row_index + 2][col + 2]
                    + lines[row_index + 3][col + 3]
                    == "MAS"
                ):
                    count += 1
                if (
                    lines[row_index][col]
                    + lines[row_index + 1][col]
                    + lines[row_index + 2][col]
                    + lines[row_index + 3][col]
                    == "MAS"
                ):
                    count += 1
                if (
                    lines[row_index][col]
                    + lines[row_index + 1][col - 1]
                    + lines[row_index + 2][col - 2]
                    + lines[row_index + 3][col - 3]
                    == "MAS"
                ):
                    count += 1

    print(count)


def part_two():
    lines = read_lines("day_4/test.txt")
    count = 0
    lines = (
        ["." * (len(lines[0]) + 8)] * 3
        + ["...." + line + "...." for line in lines]
        + ["." * (len(lines[0]) + 8)] * 3
    )
    for row_index, row in enumerate(lines):
        for col, ele in enumerate(row):
            if ele != "A":
                continue

            else:
                flag = 0

                if (
                    lines[row_index - 1][col - 1]
                    + lines[row_index][col]
                    + lines[row_index + 1][col + 1]
                    == "SAM"
                    or lines[row_index - 1][col - 1]
                    + lines[row_index][col]
                    + lines[row_index + 1][col + 1]
                    == "MAS"
                ):
                    flag += 1
                if (
                    lines[row_index + 1][col - 1]
                    + lines[row_index][col]
                    + lines[row_index - 1][col + 1]
                    == "SAM"
                    or lines[row_index + 1][col - 1]
                    + lines[row_index][col]
                    + lines[row_index - 1][col + 1]
                    == "MAS"
                ):
                    flag += 1
                if flag == 2:
                    count += 1
    print(count)


part_two()
