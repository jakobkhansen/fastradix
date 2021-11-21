import hypothesis as hyp
import hypothesis.strategies as st

from utils import successfully_sorted

def quicksort(array):
    quicksort_rec(array, 0, len(array)-1)

def quicksort_rec(array, left, right):
    if left >= right:
        return

    mid = partition(array, left, right)

    quicksort_rec(array, left, mid-1)
    quicksort_rec(array, mid+1, right)

def partition(array, left, right):
    pivot_index = pivot(array, left, right)
    pivot_value = array[pivot_index]
    array[left],array[pivot_index] = array[pivot_index],array[left]

    l = left+1
    r = right

    while l <= r:
        while l <= r and array[l] <= pivot_value:
            l += 1

        while l <= r and array[r] > pivot_value:
            r -= 1

        if l <= r:
            array[l],array[r] = array[r],array[l]

    array[left],array[r] = array[r],array[left]

    return r


def pivot(array, left, right):
    mid = (left+right) // 2
    if right - left < 3:
        return left

    a,b,c = array[left],array[mid],array[left+2]

    if a > b != a > c:
        return left
    if b < a != b < c:
        return left+1
    return left+2

