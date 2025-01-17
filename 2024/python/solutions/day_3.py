import re


def day_3(input: str, is_part_two=False):
    lines = input.strip().split("\n")
    dr = r"(do\(\)|don't\(\))"
    nr = r"mul\(\d{1,3},\d{1,3}\)"
    r = dr if is_part_two else nr

    sum = 0
    line = "".join(lines)
    search = re.findall(r, line) if not is_part_two else re.split(r, line)
    if not is_part_two:
        for el in search:
            nums = re.findall(r"\b\d{1,3}\b", el)
            sum += int(nums[0]) * int(nums[1])
    else:
        do = True
        for el in search:
            if do:
                muls = re.findall(nr, el)
                for n in muls:
                    nums = re.findall(r"\b\d{1,3}\b", n)
                    sum += int(nums[0]) * int(nums[1])
                do = el != "don't()"
            else:
                do = el != "don't()"
                continue

    print(sum)
