def find_max_subarray(array: list) -> tuple:
    max_sum = - float("inf")
    start_index = 0
    end_index = 0
    for i in range(len(array) - 1):
        current_sum = 0
        for j in range(i, len(array)):
            current_sum += array[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start_index = i
                end_index = j
    return max_sum, start_index, end_index


array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, -7]
print(find_max_subarray(array))
