def merge(left: list, right: list):
    global count
    n = len(left)
    m = len(right)
    i, j = 0, 0
    result = []
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += n - i
            j += 1
    if i == n:
        result.extend(right[j:])
    elif j == m:
        result.extend(left[i:])

    return result


def merge_sort(nums):
    if len(nums) < 2:
        return nums
    pivot = len(nums) // 2
    left = merge_sort(nums[:pivot])
    right = merge_sort(nums[pivot:])
    return merge(left, right)


count = 0
nums = [5, 4, 3, 2, 1]
merge_sort(nums)
print(count)
