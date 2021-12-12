import random


def partition(array: list, left: int, right: int):
    x = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= x:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


def quick_select(array: list, left: int, right: int, median: int):
    if left == right:
        return array[left]
    pivot = partition(array, left, right)
    len_left_sublist = pivot - left + 1
    if len_left_sublist == median:
        return array[pivot]
    elif len_left_sublist > median:
        return quick_select(array, left, pivot - 1, median)
    else:
        return quick_select(array, pivot + 1, right, median - len_left_sublist)


if __name__ == '__main__':
    lst = [random.randint(1, 20) for _ in range(10)]
    median = 4
    print(lst)
    print(quick_select(lst, 0, len(lst) - 1, median))
    print(lst)