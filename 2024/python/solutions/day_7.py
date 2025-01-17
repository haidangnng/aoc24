def check(array, current, target, pTwo=False):
    count = 0
    if len(array) == 0 and current == target:
        return True

    else:
        if len(array) > 0:
            el = array[0]

            a = check(array[1:], current * el, target, pTwo)
            b = check(array[1:], current + el, target, pTwo)

            if a:
                count += 1
            if b:
                count += 1

            if pTwo:
                c = check(array[1:], int(f"{current}{el}"), target, pTwo)
                if c:
                    count += 1

    return count


def main(lines, ispt):
    sum = 0
    for line in lines:
        [target, list] = line.split(": ")
        nums = [int(num) for num in list.split(" ")]
        count = check(nums[1:], nums[0], int(target), ispt)
        if count > 0:
            sum += int(target)

    print(sum)


def day_5(input):
    lines = input.strip().split("\n")
    main(lines, True)
    main(lines, False)
