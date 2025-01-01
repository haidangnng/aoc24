from utils import get_input
import time
from contextlib import contextmanager

# from solutions.day_1 import day_1
# from solutions.day_2 import day_2
# from solutions.day_3 import day_3
# from solutions.day_4 import day_4
# from solutions.day_5 import day_5
from solutions.day_6 import day_6


@contextmanager
def benchmark():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")


with benchmark():
    # day_1(get_input(2015, 1))
    # day_2(get_input(2015, 2))
    # day_3(get_input(2015, 3))
    # day_4("iwrupvqb")
    # day_5(get_input(2015, 5))
    day_6(get_input(2015, 6))
