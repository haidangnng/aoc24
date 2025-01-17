dir = {
    "<": [0, -1],
    ">": [0, 1],
    "^": [-1, 0],
    "v": [1, 0],
}

opts = ["^", ">", "v", "<"]


def part_one(lines):
    cd = 0
    guard = []
    matrix = (
        ["@" * len(lines[0])]
        + ["@" + line + "@" for line in lines]
        + ["@" * len(lines[0])]
    )
    matrix = [list(row) for row in matrix]
    for x, line in enumerate(matrix):
        for y, a in enumerate(line):
            if a == ">" or a == "^" or a == "<" or a == "v":
                guard = [x, y]
                cd = opts.index(a)

    [x, y] = guard
    run = True

    while run:
        step = dir[opts[cd]]
        matrix[x][y] = "X"
        next_x, next_y = x + step[0], y + step[1]
        next_val = matrix[next_x][next_y]

        if next_val == "#":
            cd = (cd + 1) % 4
        if next_val == "@":
            break

        step = dir[opts[cd]]
        x += step[0]
        y += step[1]

    count = 0
    for i in matrix:
        for j in i:
            if j == "X":
                count += 1
    print(count)


def part_two(lines):
    cd = 0
    guard = []
    matrix = (
        ["@" * len(lines[0])]
        + ["@" + line + "@" for line in lines]
        + ["@" * len(lines[0])]
    )
    matrix = [list(row) for row in matrix]
    for x, line in enumerate(matrix):
        for y, a in enumerate(line):
            if a == ">" or a == "^" or a == "<" or a == "v":
                guard = [x, y]
                cd = opts.index(a)

    [x, y] = guard
    run = True

    count = 0
    while run:
        step = dir[opts[cd]]
        temp = dir[opts[(cd + 1) % 4]]
        print(
            f"cur_dir: {opts[cd]}, next_dir: {
                opts[(cd + 1) % 4]}, temp: {temp}"
        )
        r, c = temp
        if r:
            con = [0, len(matrix)] if r > 0 else [len(matrix) - 1, 0]
            for i in range(con[0], con[1], r):
                if matrix[i][y] == "#":
                    print(f"dir: {[r, c]}, cur: {[x, y]}, block: {[i, y]}")
                    count += 1
        if c:
            con = [0, len(matrix)] if c > 0 else [len(matrix) - 1, 0]
            for i in range(con[0], con[1], c):
                if matrix[x][i] == "#":
                    print(f"dir: {[r, c]}, cur: {[x, y]}, block: {[x, i]}")
                    count += 1

        matrix[x][y] = "X"
        next_x, next_y = x + step[0], y + step[1]
        next_val = matrix[next_x][next_y]

        if next_val == "#":
            cd = (cd + 1) % 4

        if next_val == "@":
            break

        step = dir[opts[cd]]
        x += step[0]
        y += step[1]

    print(count)

    # count = 0
    # for i in matrix:
    #     for j in i:
    #         if j == "X":
    #             count += 1
    # print(count)


def day_6(input):
    lines = input.strip().split("\n")
    part_one(lines)
    part_two(lines)
