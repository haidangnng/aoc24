import hashlib


def check_no_zeros(input: str, count: int) -> bool:
    return input[:count] == "0" * count


def get_hash(input: str, counter: int) -> str:
    md5_hash = hashlib.md5(f"{input}{counter}".encode())
    hash_res = md5_hash.hexdigest()
    return hash_res


def day_4(input: str) -> None:
    counter = 0
    count = 0
    while not check_no_zeros(get_hash(input, counter), 5):
        counter += 1
    while not check_no_zeros(get_hash(input, count), 6):
        count += 1
    print(counter)
    print(count)
    return
