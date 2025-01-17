def part_one(input: str) -> None:
    left, right = [], []
    lines = input.strip().split("\n")

    res = 0

    for line in lines:
        [a, b] = line.split()
        left.append(int(a))
        right.append(int(b))

    left.sort()
    right.sort()

    for index, ele in enumerate(left):
        right_ele = right[index]
        res += abs(right_ele - ele)

    print(res)


def part_two(input: str) -> None:
    left, right = [], {}

    lines = input.strip().split("\n")
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


def day_1(input: str) -> None:
    part_one(input)
    part_two(input)
