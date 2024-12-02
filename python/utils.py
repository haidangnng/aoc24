import os

dirname = os.path.dirname(__file__)


def read_lines(fname: str) -> list[str]:
    filename = os.path.join(dirname, "../data/day_1/", fname)
    with open(filename) as f:
        return f.read().strip().splitlines()
