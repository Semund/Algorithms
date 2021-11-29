from random import randint
from timer import timer
from mergesort import merge_sort as ms
from mergesort_with_insertionsort import merge_sort as ms_ins
from heapsort import heap_sort
from quicksort import quick_sort, randomized_quick_sort


@timer
def test_ms(array: list):
    return ms(array)


@timer
def test_ms_ins(array: list):
    return ms_ins(array, 25)


@timer
def test_hs(array: list):
    heap_sort(array)


@timer
def test_qs(array):
    quick_sort(array, 0, len(array) - 1)


@timer
def test_rqs(array):
    randomized_quick_sort(array, 0, len(array) - 1)


array = [randint(1, 10000000) for _ in range(1000000)]
array2 = array[:]
ms_result = test_ms(array)
ms_ins_result = test_ms_ins(array)
test_rqs(array)
test_qs(array2)

print(array == ms_result, array == ms_ins_result, array == array2)