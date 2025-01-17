def is_safe_with_one_removal(report):
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1:]
        if is_safe_report(new_report):
            return True
    return False


def count_safe_reports(data, allow_remove=False):
    safe_count = 0
    for report in data:
        if is_safe_report(report):
            safe_count += 1
        else:
            if allow_remove:
                if is_safe_with_one_removal(report):
                    safe_count += 1
    return safe_count


def part_one(input):
    lines = input.strip().split("\n")
    data = []
    for line in lines:
        line = list(map(int, line.split()))
        data.append(line)

    print(count_safe_reports(data))


def is_safe_report(report):
    increasing = True
    decreasing = True
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False

    return increasing or decreasing


def part_two(input):
    lines = input.strip().split("\n")
    data = []
    for line in lines:
        line = list(map(int, line.split()))
        data.append(line)

    count = count_safe_reports(data, True)
    print(count)


def day_2(input: str) -> None:
    part_one(input)
    part_two(input)
