from random import randint


def merge(left: list, right: list):
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


nums = [randint(1, 10000) for _ in range(10000)]
print(merge_sort(nums) == sorted(nums))
