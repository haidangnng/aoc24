def part_one(input: str):
    lines = input.strip().split("\n")
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
                if row[col: col + 4] == "MAS":
                    count += 1
                if row[col - 3: col + 1] == "SAMX":
                    count += 1
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


def part_two(input):
    lines = input.strip().split("\n")
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


def day_3(input: str):
    part_one(input)
    part_two(input)
