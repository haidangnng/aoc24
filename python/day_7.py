from utils import read_lines


def check(array, current, target):
    count = 0
    if len(array) == 0 and current == target:
        return True

    else:
        if len(array) > 0:
            el = array[0]

            a = check(array[1:], current * el, target)
            b = check(array[1:], current + el, target)
            c = check(array[1:], int(f"{current}{el}"), target)

            if a:
                count += 1
            if b:
                count += 1
            if c:
                count += 1

    return count


def part_one():
    # lines = read_lines("day_7/test.txt")
    lines = read_lines("day_7/input.txt")
    sum = 0
    for line in lines:
        [target, list] = line.split(": ")
        nums = [int(num) for num in list.split(" ")]
        count = check(nums[1:], nums[0], int(target))
        if count > 0:
            sum += int(target)

    print(sum)


part_one()
