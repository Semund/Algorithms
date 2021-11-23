from random import randint
from insertion import insertion_sort


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


def merge_sort(nums, k=2):
    if len(nums) < k:
        return insertion_sort(nums)
    pivot = len(nums) // 2
    left = merge_sort(nums[:pivot])
    right = merge_sort(nums[pivot:])
    return merge(left, right)


if __name__ == '__main__':
    nums = [randint(1, 10000) for _ in range(10000)]
    print(merge_sort(nums) == sorted(nums))


