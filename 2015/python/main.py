from utils import get_input
import time
from contextlib import contextmanager

# from solutions.day_1 import day_1
from solutions.day_2 import day_2

@contextmanager
def benchmark():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")


with benchmark():
    # day_1(get_input(2015, 1))
    day_2(get_input(2015, 2))
