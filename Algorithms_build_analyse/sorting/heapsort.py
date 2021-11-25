def build_heap(array: list):
    n = len(array)
    for i in range(n // 2, -1, -1):
        sift_down(array, i, n)


def sift_down(array: list, index: int, size: int):
    index_max = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < size and array[left] > array[index_max]:
        index_max = left
    if right < size and array[right] > array[index_max]:
        index_max = right
    if index_max != index:
        array[index], array[index_max] = array[index_max], array[index]
        sift_down(array, index_max, size)


def heap_sort(array: list):
    build_heap(array)
    n = len(array) - 1
    for i in range(n):
        array[n - i], array[0] = array[0], array[n - i]
        sift_down(array, 0, n - i)


