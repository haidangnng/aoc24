from utils import read_lines


# Brute the fuck out of the first part
def blink(stones):
    new_stones = []
    for i in stones:
        if int(i) == 0:
            new_stones.append("1")
            continue
        if len(i) % 2 == 0:
            mid = len(i) // 2
            new_stones.append(i[:mid])
            new_stones.append(f"{int(i[mid:])}")
            continue
        new_stones.append(f"{int(i) * 2024}")

    return new_stones


def blink_blink(stone, count=0):
    if int(stone) == 0:
        return count + 1

    if len(stone) % 2 == 0:
        mid = len(i) // 2
        new_stones.append(i[:mid])
        new_stones.append(f"{int(i[mid:])}")
    return


def main():
    # lines = read_lines("day_11/test.txt")
    lines = read_lines("day_11/input.txt")
    stones = lines[0].split(" ")
    # for _ in range(0, 25):
    #     stones = blink(stones)
    for i in stones:
        blink_blink(i)

    print(len(stones))


main()
