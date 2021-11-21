
import hypothesis as hyp
import hypothesis.strategies as st
from benchmarkalgos.quicksort import quicksort
from sequential.radix_sequential import radixsort

from utils import successfully_sorted

@hyp.given(st.lists(st.integers()))
@hyp.settings(max_examples=1000)
def test_sequential_radix(array):
    radix_sorted = radixsort(array)

    assert(successfully_sorted(array, radix_sorted))

@hyp.given(st.lists(st.integers()))
@hyp.settings(max_examples=1000)
def test_quicksort(array):
    original = array.copy()
    quicksort(array)

    assert(successfully_sorted(original, array))


def usage_test():
    array = [9,5,3,7,4,1,4, 21, 97, 105, -20, -10]
    print(radixsort(array))


test_sequential_radix()
test_quicksort()
