from benchmarkalgos.quicksort import quicksort
from sequential.radix_sequential import radixsort
import timeit
import random

ARRAY_SIZES = [
    10,
    100,
    1000,
    10000,
    100000,
    1000000,
    2000000,
    3000000,
    4000000,
    5000000,
]

MIN_ELEMENT = -10000
MAX_ELEMENT = 10000

def time_radix(array):
    return timeit.timeit(lambda: radixsort(array), number=1)


def time_quicksort(array):
    return timeit.timeit(lambda: quicksort(array), number=1)

def time_timsort(array):
    return timeit.timeit(lambda: array.sort(), number=1)

def radix_vs_quick():
    print("--- Sequential Radix vs. Sequential Quicksort")

    for n in ARRAY_SIZES:
        array = [random.randint(MIN_ELEMENT, MAX_ELEMENT) for _ in range(n)]
        radix = array.copy()
        quick = array.copy()
        print(f"\n--- n = {n}")
        print("Radix:", time_radix(radix))
        print("Quicksort:", time_quicksort(quick))


if __name__ == "__main__":
    radix_vs_quick()
