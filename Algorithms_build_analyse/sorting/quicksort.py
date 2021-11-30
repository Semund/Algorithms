import random
from random import randint


def lomuto_partition(array: list, left: int, right: int):
    x = array[right]
    i = left - 1
    for j in range(left, right, 1):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


def quick_sort(array: list, begin: int, end: int):
    if begin < end:
        pivot = lomuto_partition(array, begin, end)
        quick_sort(array, begin, pivot - 1)
        quick_sort(array, pivot + 1, end)


def randomized_quick_sort(array: list, begin: int, end: int):
    if begin < end:
        pivot = randomized_partition(array, begin, end)
        randomized_quick_sort(array, begin, pivot - 1)
        randomized_quick_sort(array, pivot + 1, end)


def randomized_partition(array: list, left: int, right: int):
    i = random.randint(left, right)
    array[i], array[right] = array[right], array[i]
    return lomuto_partition(array, left, right)


def hoare_quick_sort(array: list, left: int, right: int):
    if left < right:
        x = array[right]
        i = left
        j = right
        while i <= j:
            while array[i] < x:
                i += 1
            while array[j] > x:
                j -= 1
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        hoare_quick_sort(array, left, j)
        hoare_quick_sort(array, i, right)


if __name__ == '__main__':
    lst = [randint(1, 100000) for _ in range(1000000)]
    lst_copy1 = lst[:]
    lst_copy2 = lst[:]
    quick_sort(lst, 0, len(lst) - 1)
    randomized_quick_sort(lst_copy1, 0, len(lst_copy1) - 1)
    hoare_quick_sort(lst_copy2, 0, len(lst_copy2) - 1)
    print(lst == lst_copy1, lst == lst_copy2)
