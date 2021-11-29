from random import randint


def partition(array: list, left: int, right: int):
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
        pivot = partition(array, begin, end)
        quick_sort(array, begin, pivot - 1)
        quick_sort(array, pivot + 1, end)


if __name__ == '__main__':
    lst = [randint(1, 100000) for _ in range(1000000)]
    test = sorted(lst[:])
    quick_sort(lst, 0, len(lst) - 1)
    print(lst == test)
