def find_max_subarray(array: list) -> tuple:
    array_with_sums = [0] + [0] * len(array)
    max_sum = - float("inf")
    current_sum = 0
    right_index = 0
    for i in range(len(array)):
        current_sum += array[i]
        if current_sum > 0:
            array_with_sums[i + 1] = current_sum
            if current_sum > max_sum:
                max_sum = current_sum
                right_index = i
        else:
            current_sum = 0
    i = right_index
    while array_with_sums[i] != 0:
        i -= 1
    left_index = i
    return max_sum, left_index, right_index


array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, -7]
print(find_max_subarray(array))
