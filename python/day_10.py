from utils import read_lines

dir = [
    [0, 1],  # RIGHT
    [0, -1],  # LEFT
    [1, 0],  # DOWN
    [-1, 0],  # UP
]


def trail(matrix, cur):
    print(cur)
    for x, y in dir:
        trail(matrix, matrix[x][y])

    return


def main():
    lines = read_lines("day_10/test.txt")
    # lines = read_lines("day_10/input.txt")
    for x, r in enumerate(lines):
        for y, val in enumerate(r):
            if int(val) == 0:
                trail(lines, [x, y])


main()
