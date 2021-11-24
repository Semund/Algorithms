def find_max_crossing_subarray(array: list, start: int, end: int, mid: int) -> tuple:
    left_sum = - float("inf")
    right_sum = - float("inf")
    sum = 0
    left_index, right_index = None, None
    for i in range(mid, start - 1, -1):
        sum += array[i]
        if sum > left_sum:
            left_sum = sum
            left_index = i
    sum = 0
    for j in range(mid + 1, end + 1):
        sum += array[j]
        if sum > right_sum:
            right_sum = sum
            right_index = j
    return left_sum + right_sum, left_index, right_index


def find_max_subarray(array: list, start: int, end: int) -> tuple:
    """
    The function searches for a subarray with the maximum sum of elements in the input array. Difficult O(nlgn).
    The subarray can be found in the left half, right half, or with an intersection in the middle of the original array.
    :param array: input array
    :param start: start-index of array
    :param end: end-index of array
    :return: tuple with the sum of the elements, the start-index and the end-index.
    """
    results = dict()
    if start == end:
        return array[start], start, end
    else:
        mid = (start + end) // 2
        results["left"] = find_max_subarray(array, 0, mid)
        results["right"] = find_max_subarray(array, mid + 1, end)
        results["cross"] = find_max_crossing_subarray(array, start, end, mid)
        return max(results.values(), key=lambda x: x[0])


array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, -7]
print(find_max_subarray(array, 0, len(array) - 1))


