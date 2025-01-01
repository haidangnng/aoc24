directions = {
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
}


def get_next(current, dir) -> (int, int):
    (cur_x, cur_y) = current
    (dir_x, dir_y) = dir
    next = (cur_x + dir_x, cur_y + dir_y)
    return next


def part_1(input: str) -> None:
    houses = set()
    current = (0, 0)

    for i in input:
        next = get_next(current, directions[i])
        houses.add(next)
        current = next

    print(f"part_1: {len(houses)}")


def part_2(input: str) -> None:
    houses = set()
    current_santa = (0, 0)
    current_robot = (0, 0)

    for i in range(0, len(input), 2):
        next_santa = get_next(current_santa, directions[input[i]])
        next_robot = get_next(current_robot, directions[input[i + 1]])
        houses.add(next_santa)
        houses.add(next_robot)
        current_santa = next_santa
        current_robot = next_robot

    print(f"part_2: {len(houses)}")


def day_3(input: str) -> None:
    part_1(input)
    part_2(input)

    return
