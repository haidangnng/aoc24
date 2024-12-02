from utils import read_lines


def part_one():
    left, right = [], []

    lines = read_lines("day_1/input.txt")
    for line in lines:
        [a, b] = line.split()
        left.append(int(a))
        right.append(int(b))

    left.sort()
    right.sort()

    sum = 0
    for index, ele in enumerate(left):
        right_ele = right[index]
        sum += abs(right_ele - ele)

    print(sum)


def part_two():
    left, right = [], {}

    lines = read_lines("day_1/input.txt")
    for line in lines:
        [a, b] = line.split()
        left.append(int(a))
        b = int(b)
        if b not in right:
            right[b] = 1
        else:
            right[b] = right[b] + 1

    sum = 0
    for i in left:
        num = right.get(i) if right.get(i) else 0
        sum += i * num

    print(sum)


part_two()
