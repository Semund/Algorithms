def merge(array: list, start: int, middle: int, end: int):
    n1 = middle - start + 1
    n2 = end - middle
    left_array = [0] * n1
    right_array = [0] * n2

    for i in range(n1):
        left_array[i] = array[start + i]

    for j in range(n2):
        right_array[j] = array[middle + 1 + j]

    i, j = 0, 0
    k = start
    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(array: list, start: int, end: int):
    if start < end:
        middle = (start + end) // 2
        merge_sort(array, start, middle)
        merge_sort(array, middle + 1, end)
        merge(array, start, middle, end)





